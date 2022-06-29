import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

s = Service("C:/Users/Bestpeers/PycharmProjects/seleniumPython/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://demo.automationtesting.in/Slider.html')
print('Homepage : ', driver.title)
driver.maximize_window()
driver.implicitly_wait(time_to_wait=5)

slider = driver.find_element(by=By.XPATH, value="//div[@id='slider']")
move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(45, 0).release().perform()