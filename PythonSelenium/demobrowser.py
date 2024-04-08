import time

from selenium import webdriver

# Chrome driver service
# driver = webdriver.Chrome()

# Chrome driver service
driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
# browser title in the tab
print(driver.title)
print(driver.current_url)
time.sleep(10)