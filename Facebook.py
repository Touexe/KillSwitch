from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

import json

class Facebook:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.options = Options()
        self.base_desktop_url = "https://facebook.com"
    
    def initiate_browser(self):
        self.driver = webdriver.Chrome(chrome_options=self.options, executable_path=r'\drivers\chromedriver.exe') 
        #driver = webdriver.Chrome(chrome_options=self.options)
        return self.driver 
        
    def login(self):
        driver = self.driver
        driver.get(f"{self.base_desktop_url}")  
         
        Username_element = driver.find_element_by_id("email")
        Password_element = driver.find_element_by_id("pass")
        
        Username_element.send_keys(self.username)
        Password_element.send_keys(self.password)
        Submit = driver.find_element_by_name("login").send_keys(Keys.ENTER)
    def deactivate(self):

    
    
    
