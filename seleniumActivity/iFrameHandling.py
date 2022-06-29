import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

s = Service("C:/Users/Bestpeers/PycharmProjects/seleniumPython/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://demo.automationtesting.in/Frames.html')
print('Homepage : ', driver.title)
driver.maximize_window()
driver.implicitly_wait(time_to_wait=5)

driver.switch_to.frame(driver.find_element(by=By.ID, value="singleframe"))
time.sleep(2)
driver.find_element(by=By.XPATH, value="//input[@type='text']").send_keys("Rakesh Singh Thakur")
time.sleep(2)
driver.switch_to.parent_frame()
time.sleep(2)
driver.find_element(by=By.XPATH, value="//a[normalize-space()='Iframe with in an Iframe']").click()
time.sleep(2)

driver.switch_to.frame(driver.find_element(by=By.XPATH, value="//body/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/iframe[1]"))
time.sleep(2)
driver.switch_to.frame(driver.find_element(by=By.XPATH, value="/html[1]/body[1]/section[1]/div[1]/div[1]/iframe[1]"))
time.sleep(2)
driver.find_element(by=By.XPATH, value="//body[1]/section[1]/div[1]/div[1]/div[1]/input[1]").send_keys("Rakesh Singh Thakur")
time.sleep(2)
