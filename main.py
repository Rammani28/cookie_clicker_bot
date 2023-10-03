import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# EXECUTABLE_PATH = '~/Downloads/chromedriver/chromedriver-linux64/chromedriver'
URL = "https://orteil.dashnet.org/cookieclicker/"
BREAK = 15
COUNT = 5
FACTOR = 0.1  # 20 %
INITIAL_BREAK = 50  # 60 sec to configure/load existing game


driver = webdriver.Chrome()
driver.get(URL)

def save():
    save_btn = driver.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[3]/a')
    save_btn.click()
    print("saved..")

def click_options():
    options = driver.find_element(By.CLASS_NAME, "subButton")
    options.click()

def show_status(i: int, one_set: int):

    percent = int(i/COUNT*100)
    print(f"{percent} % clicked")
    time.sleep(0.15)


def take_break(n):
    print(f"break for {n} seconds started")
    for i in range(n):
        print(f"{n-i-1} sec remaining")
        time.sleep(1)


def get_stat():
    cookies = driver.find_element(By.ID, "cookies")
    cookies_count = cookies.text.split()[0]
    production_rate = cookies.text.split()[-1]
    

def buy_item():
    store = driver.find_elements(By.CSS_SELECTOR, "#products .enabled")
    store[-1].click()


def click_cookie():
    global COUNT
    cookie_btn = driver.find_element(by=By.ID, value="bigCookie")
    i=0
    COUNT = int(COUNT * (1 + FACTOR))
    
    while i<COUNT:
        one_set = 4/COUNT * 100
        if i%one_set==0:
            show_status(i, int(one_set))
        
        cookie_btn.click()
        i+=1


def main():
    take_break(INITIAL_BREAK)
    click_options()
    i=1
    while True:
        print(f"iteration {i} for {COUNT} clicks started..")
        click_cookie()
        take_break(BREAK)
        try:
            buy_item()
        except:
            pass
        save()
        i+=1

    driver.quit()

main()