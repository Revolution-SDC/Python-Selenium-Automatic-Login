# Automated instagram login using Selenium

from selenium import webdriver #pip install selenium
import time

username = 'username' # Change to your username here
password = 'password' # Change to your password here
url='https://www.instagram.com/'
driver = webdriver.Chrome("./chromedriver")
driver.get(url)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

#the part of code that isn't in the post
time.sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
