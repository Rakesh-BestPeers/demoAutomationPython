import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/Bestpeers/PycharmProjects/seleniumPython/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://demo.automationtesting.in/AutoComplete.html')
print('Homepage : ', driver.title)
driver.maximize_window()
driver.implicitly_wait(time_to_wait=5)

search_box = driver.find_element(by=By.XPATH, value="//input[@id='searchbox']")
search_box.send_keys('N')  # Type in selenium.
time.sleep(1)
search_box.send_keys(Keys.ARROW_DOWN)  # Press ARROW_DOWN key.
time.sleep(1)
search_box.send_keys(Keys.ARROW_DOWN)  # Press ARROW_DOWN key.
time.sleep(1)
search_box.send_keys(Keys.ARROW_DOWN)  # Press ARROW_DOWN key.
time.sleep(3)
search_box.send_keys(Keys.ENTER)
time.sleep(1)
search_box.send_keys('Mala')  # Type in selenium.
time.sleep(1)
search_box.send_keys(Keys.ARROW_DOWN)  # Press ARROW_DOWN key.
time.sleep(1)
search_box.send_keys(Keys.ARROW_DOWN)  # Press ARROW_DOWN key.
time.sleep(1)
search_box.send_keys(Keys.ARROW_DOWN)  # Press ARROW_DOWN key.
time.sleep(3)
search_box.send_keys(Keys.ENTER)
