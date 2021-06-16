from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


class InstagramBot:


    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(r'E:\Projects\Instragram bot\chromedriver.exe')
        self.login()


    def login(self):
        self.driver.get('https://instagram.com/accounts/login')
        sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)

    def nav_user(self,user):
        sleep(2)
        self.driver.get('https://instagram.com/' + user)

    
    def follow_user(self,user):
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0]
        follow_button.click()


    def like_user_post(self,user,limit = 3):
        self.nav_user(user)
        photo = self.driver.find_elements_by_class_name('eLAPa')[0]
        photo.click()
        sleep(6)
        for i in range(limit):
            like_btn = self.driver.find_elements_by_class_name('wpO6b')[2]
            like_btn.click()
            sleep(2) 
            next_btn = self.driver.find_elements_by_xpath("//a[contains(text(),'Next')]")[0]
            next_btn.click()
            sleep(2)

    def like_tag_post(self,tag,limit=5):
        sleep(2)
        self.driver.get('https://instagram.com/explore/tags/' +tag)
        sleep(2)
        photo = self.driver.find_elements_by_class_name('eLAPa')[0]
        photo.click()
        sleep(6)
        for i in range(limit):
            like_btn = self.driver.find_elements_by_class_name('wpO6b')[1]
            like_btn.click()
            sleep(2) 
            next_btn = self.driver.find_elements_by_xpath("//a[contains(text(),'Next')]")[0]
            next_btn.click()
            sleep(2)

    def comment_user_post(self, user, comment):
        try:
            self.nav_user(user)
            sleep(2)
            photo = self.driver.find_elements_by_class_name('eLAPa')[0]
            photo.click()
            sleep(2)
            comment_button = bot.driver.find_element_by_class_name('_JgwE')
            comment_button.click()
            sleep(2)
            comment_field = self.driver.find_element_by_class_name('Ypffh')
            sleep(2)
            comment_field.send_keys(comment)
            sleep(2)
            post = self.driver.find_element_by_xpath('//button[contains(text(), "Post")]')
            post.click()
        except:
            pass


bot = InstagramBot('mitesh_bot','mpsingh8199')
bot.comment_user_post('sonpal_2106','Great pic dude!')

