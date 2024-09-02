from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://sandz0814.github.io/Tribu-Sinag-Padayon.com/')

x = driver.find_element(By.CSS_SELECTOR, "body header footer p")
print(x.text)

time.sleep(10)