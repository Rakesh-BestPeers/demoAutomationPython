import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:/Users/Bestpeers/PycharmProjects/seleniumPython/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://jqueryui.com/tooltip/')
print('Homepage : ', driver.title)
driver.maximize_window()
driver.implicitly_wait(time_to_wait=5)

driver.switch_to.frame(driver.find_element(by=By.XPATH,
                                           value="//body/div[@id='container']/div[@id='content-wrapper']/div[1]/div[1]/iframe[1]"))
time.sleep(2)
toolTip = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='age']")))
hov = ActionChains(driver).move_to_element(toolTip)
txt = hov.perform()
tooltipText = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@title='We ask for your age only for statistical purposes.']"))).text
print(tooltipText)
