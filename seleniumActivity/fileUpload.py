import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

s = Service("C:/Users/Bestpeers/PycharmProjects/seleniumPython/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://demo.automationtesting.in/FileUpload.html')
print('Homepage : ', driver.title)
driver.maximize_window()
driver.implicitly_wait(time_to_wait=5)

uploadFile = driver.find_element(by=By.XPATH, value="//input[@id='input-4']")
uploadFile.send_keys("C:\\Users\\Bestpeers\\Music\\ProfilePicturePhoto.jpg")
