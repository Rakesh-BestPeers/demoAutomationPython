import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/Bestpeers/PycharmProjects/seleniumPython/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://demo.automationtesting.in/Register.html')
driver.maximize_window()
driver.implicitly_wait(time_to_wait=5)
driver.find_element(by=By.XPATH, value="//input[@placeholder='First Name']").send_keys("Automation")
time.sleep(2)
driver.find_element(by=By.XPATH, value="//input[@placeholder='Last Name']").send_keys("Engineer")
time.sleep(2)
driver.find_element(by=By.XPATH, value="//textarea[@class='form-control ng-pristine ng-untouched ng-valid']").send_keys(
    "AB Road, Scheme No 53, Indore, 452056, Madhya Pradesh, India")
time.sleep(2)
driver.find_element(by=By.XPATH, value="//input[@type='email']").send_keys("Engineer@mailnesia.com")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
