import time
from selenium import webdriver



# Assigning the browser variable with chromedriver of Chrome.
# Any other browser and its respective webdriver
# like geckodriver for Mozilla Firefox can be used
browser = webdriver.Chrome('chromedriver')

browser.get("https://www.instagram.com/")

time.sleep(20)


username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')

username.send_keys("instagram_username")
password.send_keys("instagram_password")

#time.sleep(3)

login = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
login.click()

time.sleep(100)

browser.close()
