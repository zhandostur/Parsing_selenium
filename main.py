import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.olx.kz/d/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/q-xiaomi-redmi-note-9s/')
time.sleep(5)
browser.save_screenshot('1.png')