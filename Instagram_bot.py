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
        sleep(5)

        #click not now button 
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")\
            .click()
        sleep(2)
     
    def get_names_follow(self):
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
            links = scroll_box.find_elements_by_tag_name('a')

        for name in links:
            if name.text != '':
                names.append(name.text)

        #click close button
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')\
            .click()
        
        return names

    def get_names_like(self):

        
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div')

        ht,last_ht = 1,0
        links=[]
        names=[]
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            #scroll down until bottom
            ht = self.driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight);return arguments[0].scrollHeight;',scroll_box)
            
            #get names and put into a list
            links = scroll_box.find_elements_by_tag_name('a')
            for name in links:
                if name.text !='' and name.text not in names:
                    names.append(name.text)
                

        #click close button
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div[2]/button')\
            .click()
        print('likes = ',len(names))
        return names
    
    def get_followers(self):
        
        #click followers button
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')\
            .click()

        #get name of followers
        followers = self.get_names_follow()
        sleep(1)
        
        print('followers = ',len(followers))

        return followers

    def get_following(self):

         #click following button
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')\
            .click()
        
        #get names of followings
        followings = self.get_names_follow()

        print('followwings = ',len(followings))

        return followings



    def get_unfollowers(self):

        #click profile button and go to profile page
        navBar = self.driver.find_element_by_class_name('_47KiJ')
        self.driver.execute_script('return arguments[0].lastChild',navBar)\
            .click()


        #get followers
        followers = self.get_followers()

        #get followings
        followings = self.get_following()
        
        #create a list which contains names who are not following back
        not_following_back = [user for user in followings if user not in followers]

        print(not_following_back)

    def get_last_post(self):

        #click profile button and go to profile page
        navBar = self.driver.find_element_by_class_name('_47KiJ')
        self.driver.execute_script('return arguments[0].lastChild',navBar)\
            .click()
        sleep(2)

        #click last post
        article = self.driver.execute_script("return document.querySelector('.v1Nh3')")\
            .click()
        sleep(2)

    def get_liked_by(self):
        
        #click liked by button
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[1]/button')\
            .click()
        sleep(2)

        #get names who like 
        likedBy = self.get_names_like()

        #click close button
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/button')\
           .click()

        return likedBy
        
    def find_ghost_followers(self):
        
        #get last post
        self.get_last_post()

        #get liked by
        likedBy = self.get_liked_by()

        #get followers
        followers = self.get_followers()

        #create a list which contains names who follow you but don't like your photo
        ghost_followers = [user for user in followers if user not in likedBy]

        print(ghost_followers)



#username = input('username=')
#password = input('password=')
username = 'kursadguzelkaya'
password = 'Kürşad2001.'


my_bot = InstaBot(username,password)


#my_bot.get_unfollowers()

my_bot.find_ghost_followers()