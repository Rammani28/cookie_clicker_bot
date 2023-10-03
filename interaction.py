import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome()
driver.get(URL)

count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
print(count.text)


anyone_can_edit = driver.find_element(by=By.LINK_TEXT, value="anyone can edit")
anyone_can_edit.click()



time.sleep(5)

driver.quit()