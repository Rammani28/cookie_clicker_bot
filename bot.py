import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# EXECUTABLE_PATH = '~/Downloads/chromedriver/chromedriver-linux64/chromedriver'
URL = "https://orteil.dashnet.org/cookieclicker/"


class Bot:
    driver = webdriver.Chrome()
    driver.get(URL)
    cookie_btn = driver.find_element(By.ID, "bigCookie")
    store = driver.find_element(By.ID, "store")
    products = driver.find_element(By.ID, "products")

    def click_1000_times(self):
        i=0
        while i < 1000:
            self.cookie_btn.click()
            self.cookie_btn.click()
            self.cookie_btn.click()
            i+=3
        
    def check_product(self):
        
        pass

bot = Bot()
time.sleep(10)
bot.click_1000_times()
bot.check_product()


time.sleep(10)
bot.driver.quit()