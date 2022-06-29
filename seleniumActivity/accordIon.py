import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

s = Service("C:/Users/Bestpeers/PycharmProjects/seleniumPython/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://demo.automationtesting.in/Accordion.html')
print('Homepage : ', driver.title)
driver.maximize_window()
driver.implicitly_wait(time_to_wait=5)

head1 = driver.find_element(by=By.XPATH, value="(//div[@class='panel-heading'])[1]")
print('Heading_1 :: ', head1.text)
text1 = driver.find_element(by=By.XPATH, value="//div[@id='collapse1']//div[1]")
print('collapse_1 :: ', text1.text)
time.sleep(2)

head2 = driver.find_element(by=By.XPATH, value="(//div[@class='panel-heading'])[2]")
print('Heading_2 ::', head2.text)
head2.click()
text2 = driver.find_element(by=By.XPATH, value="//div[@id='collapse2']//div[1]")
print('collapse_2 ::', text2.text)
time.sleep(2)

head3 = driver.find_element(by=By.XPATH, value="(//div[@class='panel-heading'])[3]")
print('Heading_3 ::', head3.text)
head3.click()
text3 = driver.find_element(by=By.XPATH, value="//div[@id='collapse3']//div[1]")
print('collapse_3 ::', text3.text)
time.sleep(2)

head4 = driver.find_element(by=By.XPATH, value="(//div[@class='panel-heading'])[4]")
print('Heading_4 ::', head4.text)
head4.click()
text4 = driver.find_element(by=By.XPATH, value="//div[@id='collapse4']//div[1]")
print('collapse_4 ::', text4.text)
time.sleep(2)
