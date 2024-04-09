import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome driver service
driver = webdriver.Chrome()

# Chrome driver service
#driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# browser title in the tab
print(driver.title)
print(driver.current_url)

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "name").send_keys("HELLO")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()


time.sleep(10)

