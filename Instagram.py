from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.common.exceptions import NoSuchElementException

import time

import json

class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.options = Options()      
        self.base_desktop_url = "https://Instagram.com"
    
    def initiate_browser(self):
        self.options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        self.driver = webdriver.Chrome(options=self.options, executable_path=r'\drivers\chromedriver.exe') 
        #driver = webdriver.Chrome(chrome_options=self.options)
        return self.driver 
        
    def login(self):   
        driver = self.driver
        driver.get(f"{self.base_desktop_url}")  
        
        driver.implicitly_wait(1)
        Username_element = driver.find_element_by_name("username")
        Password_element = driver.find_element_by_name("password")
        
        Username_element.send_keys(self.username)
        Password_element.send_keys(self.password)
        Submit = driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.implicitly_wait(1)
        try:
            Error = driver.find_element_by_xpath("//p[@data-testid='login-error-message']")
            print(Error.text)  
            driver.close()          
        except NoSuchElementException:
            print("NO?")
            pass
        
        wait_until_logged_in = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//article[@role='presentation']")))
                
    def deactivate(self):
        driver = self.driver
        driver.get(f"{self.base_desktop_url}/accounts/remove/request/temporary/")
        
        select_element = Select(driver.find_element_by_id("deletion-reason"))
        select_element.select_by_value ("need-break")
        
        Password_element = driver.find_element_by_id("password")
        Password_element.send_keys(self.password)
        
        driver.implicitly_wait(1)
        deactivate_button = driver.find_element_by_xpath("//button[@type='button'][text() = 'Temporarily Disable Account']").click()
        
        yes_button = driver.find_element_by_xpath("//button[@type='button'][text() = 'Yes']").click()
        
        wait_until_succeed = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Sign up")))
        print("Succeed!")
    
bot = Instagram("011426166","250799")
bot.initiate_browser()
bot.login()
bot.deactivate()

    
    
    
