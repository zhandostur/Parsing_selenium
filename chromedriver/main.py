from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options, executable_path='/home/zhandos/Parsing_selenium/chromedriver/chromedriver')
url = 'https://www.instagram.com/accounts/login/?__coig_restricted=1'

browser.get(url=url)
xpath_username = '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input'
time.sleep(5)
