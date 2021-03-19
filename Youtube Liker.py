from selenium import webdriver

# Path to chrome web driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
# Init driver and pass on the PATH
driver = webdriver.Chrome(PATH)

# Pass on the website
# Opens the Website
driver.get("https://www.youtube.com/watch?v=F5mRW0jo-U4")

print(driver.title)

# Search an element on the page using Name. In this case Input field with name = "S"
search = driver.find_element_by_class_name("style-scope yt-icon-button")
# Clear the Input Field
# search.clear()
# Send Input to Search
# search.send_keys(["Test", Keys.RETURN])
print(search.tag_name)
search.click()
# Send "ENTER" to Search
# search.send_keys(Keys.RETURN)
