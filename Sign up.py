
from selenium import webdriver
#driver = webdriver.Firefox(executable_path="driver/geckodriver.exe")
driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.get('http://www.chykalophia.com')

driver.maximize_window()

#Email field imput

email_field_input = driver.find_element_by_xpath('//input[@id="ff_3_email"]')
email_field_input.clear()
email_field_input.send_keys("luda@gmail.com")

#subbmit button
subbmit_button = driver.find_element_by_xpath('//button[@class="ff-btn-subbmit"]')
subbmit_button.click()

driver.close()
