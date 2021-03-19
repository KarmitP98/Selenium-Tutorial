import time

from selenium import webdriver
# Path to chrome web driver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
# Init driver and pass on the PATH
driver = webdriver.Chrome(PATH)

# Pass on the website
# Opens the Website
login_url = "http://192.168.0.1/webpages/login.html"
sleep_time = 1
driver.get(login_url)
print(driver.title)

driver.maximize_window()


def login():
    time.sleep(sleep_time)
    input_login = driver.find_element_by_id("user_login")
    input_password = driver.find_element_by_id("user_password")
    button_login = driver.find_element_by_id("btnLogin")
    input_login.send_keys(["cusadmin", Keys.TAB])
    input_password.send_keys(["open1234", Keys.TAB])
    button_login.click()


def navigate_to_filter():
    time.sleep(sleep_time * 3)
    a_security = driver.find_element_by_xpath('//a[@href="#security_firewall/m/5/s/0"]')
    a_security.click()

    time.sleep(sleep_time)

    a_keyword_filter = driver.find_element_by_link_text("Keyword Filter")
    a_keyword_filter.click()

    lines = open("list_v2.txt", "r")
    for line in lines:
        print(line)
        add_KeyWord(line)

    save()


def add_KeyWord(line):
    time.sleep(sleep_time)
    button_add = driver.find_element_by_id("Button_Add")
    button_add.click()

    time.sleep(sleep_time)
    input_name = driver.find_element_by_name("kwdName")
    input_name.send_keys([line])

    button_apply = driver.find_element_by_id("btnApply")
    button_apply.click()


def save():
    time.sleep(sleep_time * 2)
    button_save = driver.find_element_by_id("Button_Save")
    button_save.click()

    logOut()


def logOut():
    time.sleep(sleep_time * 10)
    a_log_out = driver.find_element_by_id("titleid")
    a_log_out.click()

    time.sleep(sleep_time)
    button_log_out = driver.find_element_by_id("btnLogout")
    button_log_out.click()

    print("Successfully added all the lines!")


login()
navigate_to_filter()

