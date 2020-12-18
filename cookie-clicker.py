from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

WAIT = 5

# Path to chrome web driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
# Init driver and pass on the PATH
driver = webdriver.Chrome(PATH)

# Pass on the website
# Opens the Website
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Implicitely wait x seconds
driver.implicitly_wait(WAIT)  # seconds

bigCookie = driver.find_element_by_id("bigCookie")
cokies = driver.find_element_by_id("cookies")
# Get all the items
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)

# Action to click on element bigCookie
actions.click(bigCookie)

for i in range(5000):
    # Perform the action
    actions.perform()
    # Split the word and get the first number
    count = int(cokies.text.split(" ")[0])
    print(count)

    for item in items:
        # Get the value of the upgradable
        value = int(("").join(item.text.split(",")))
        # If Upgrade it cheaper than cookie
        if value <= count:
            # Define a new action chain
            upgrade_actions = ActionChains(driver)
            # Move the cursor to the item and click
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()


# Build your actions
# actions.click()
# actions.perform()
