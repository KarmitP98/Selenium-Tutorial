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
# driver.get("https://smart-shoppers-2a1ab.firebaseapp.com/login")

# print(driver.title)

# Search an element on the page using Name. In this case Input field with name = "S"
search = driver.find_element_by_name("s")
# Clear the Input Field
search.clear()
# Send Input to Search
search.send_keys(["Test", Keys.RETURN])
# Send "ENTER" to Search
# search.send_keys(Keys.RETURN)

# ----------------------- NEXT PAGE ----------------------------- #

# Wait till the element is present
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # Find all article element in main
    articles = main.find_elements_by_tag_name("article")
    # Loop through all the article titles
    for article in articles:
        # Print the Text inside Article.entry-summery class
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    driver.quit()

# print(main.text)

# # Wait 5 secs
# time.sleep(5)
# # Closes the current TAB
# driver.close()

# Closes the browser
# driver.quit()
