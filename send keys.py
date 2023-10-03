import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome()
driver.get(URL)

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("First name")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("last name")

email = driver.find_element(By.NAME, "email")
email.send_keys("sth@sth.com")

sign_up = driver.find_element(By.CLASS_NAME, "btn-block")
sign_up.click()

time.sleep(5)
driver.quit()