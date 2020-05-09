from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self,username,pasword):
        self.username=username
        self.pasword=pasword

        #go to webpage
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.instagram.com/')
        sleep(2)

        #write username
        self.driver.find_element_by_xpath('//input[@name=\'username\']')\
            .send_keys(username)

        #write password
        self.driver.find_element_by_xpath('//input[@name=\'password\']')\
            .send_keys(pasword)

        #click log in button
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')\
            .click()
        sleep(2)

        #click not now button 
        
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")\
            .click()
        sleep(2)
     

        #click profile button and go to profile page
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]')\
            .click()
        sleep(2)



    def get_unfollowers(self):
        #click followers button
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')\
            .click()
        #get name of followers
        followers = self.get_names()
        
        sleep(1)
        #click following button
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')\
            .click()
        
        #get names of followings
        followings = self.get_names()

        #create a list which contains names who are not following back
        not_following_back = [user for user in followings if user not in followers]
        print(not_following_back)

        
    def get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')

        
        ht,last_ht = 1,0
        links=[]
        names=[]
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            #scroll down until bottom
            ht = self.driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight);return arguments[0].scrollHeight;',scroll_box)
            
            #get names and put into a list
            links = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]').find_elements_by_tag_name('a')
            names = [name.text for name in links if name.text !='']

        #click close button
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')\
            .click()
        
        return names

username = input('username=')
password = input('password=')


#my_bot = InstaBot('dr.metegzlky','7142128')
my_bot = InstaBot(username,password)
my_bot.get_unfollowers()