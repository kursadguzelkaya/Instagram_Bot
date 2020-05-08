from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self,username,pasword):
        self.username=username
        self.pasword=pasword

        self.driver=webdriver.Chrome()
        self.driver.get('https://www.instagram.com/')
        sleep(2)

        self.driver.find_element_by_xpath('//input[@name=\'username\']')\
            .send_keys(username)

        self.driver.find_element_by_xpath('//input[@name=\'password\']')\
            .send_keys(pasword)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')\
            .click()
        #sleep(10)

        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]")\
            .click()
        sleep(5)


InstaBot('kursadguzelkaya','Kürşad2001.')