from selenium import webdriver
import time
options = webdriver.FirefoxOptions()
browser = webdriver.Firefox(options=options)
url = 'https://www.olx.kz/d/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/q-xiaomi-redmi-note-9s/'

browser.get(url=url)
button = browser.fin