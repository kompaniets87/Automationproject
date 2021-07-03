from selenium import webdriver

#driver = webdriver.Firefox(executable_path="driver/geckodriver.exe")
driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.get('http://www.chykalophia.com')

#cookie policy
cookie_button = driver.find_element_by_xpath("//a[@)href='https://www.iubenda.com/privacy-policy/32384925/cookie-policy']")
cookie_button.click()
driver.close()