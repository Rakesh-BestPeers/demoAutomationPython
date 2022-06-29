import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Screenshot import Screenshot_Clipping
from PIL import Image

s = Service("C:/Users/Bestpeers/PycharmProjects/seleniumPython/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.geeksforgeeks.org/')
print('Homepage : ', driver.title)
driver.maximize_window()
driver.implicitly_wait(time_to_wait=5)

a = ActionChains(driver)
widget = driver.find_element(by=By.XPATH, value="//body[1]/div[1]/div[1]/ul[1]/li[3]/span[1]")
a.move_to_element(widget).perform()
autoComplete = driver.find_element(by=By.LINK_TEXT, value="Apply for Jobs")
time.sleep(2)
a.move_to_element(autoComplete).click().perform()
print('Jobs : ', driver.title)

driver.save_screenshot("C:/Users/Bestpeers/PycharmProjects/seleniumPython/Screenshots/ss.png")
screenshot = Image.open("C:/Users/Bestpeers/PycharmProjects/seleniumPython/Screenshots/ss.png")
driver.close()