from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to chrome web driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
# Init driver and pass on the PATH
driver = webdriver.Chrome(PATH)

# Pass on the website
# Opens the Website
driver.get("https://techwithtim.net")

# Access the element by text inside link element
link = driver.find_element_by_link_text("Python Programming")
# Click on the link
link.click()

# NOTE: Ideally you want to wait for the element to be loaded!!!

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    # Wait for Button with id
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    # GO back 3 times to home page
    driver.back()
    driver.back()
    driver.back()

    # Go Forward
    # driver.forward()

except:
    driver.quit()
