from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://sandz0814.github.io/sandz/Contact.html')

x = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(2) td:nth-child(2)")
print(x.text)

time.sleep(10)