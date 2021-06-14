from selenium import webdriver


driver = webdriver.Chrome(executable_path="Driver\chromedriver.exe")
driver = webdriver.Chrome(executable_path="Driver\gechodriver.exe")
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver_maximaze_window()

logo = driver_find_element_by_xpath("//img[@title='Brainbucket']")

newregistrantbtn = driver_find_Element_by_xpath("//a[contains(text)), 'Continue')]")
new_registran_tbtn.click()

#Register account
#Personal details
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Lana")
driver.quit()

#Email field
firstname_field = driver.find_element_by_id("input-email")
firstname_input.clear()
firstname_input.send_keys("Luda@gmail.com")

#Password field
firstname_field = driver.find_element_by_id("input-password")
firstname_input.claer()
firstname_input.send_keys("12345")

firstname_field = driver.find_element_by_id("input-lastname")
firstname_input.clear()
firstname_input.clear("Maks")

first_field = driver.find_element_by_id("input-email")
firstname_input.clear()
firstname_input.clear("Luda@gmail.com")

firstname_field = driver.find_element_by_id("input-telephone")
firstname_input.clear()
firstname_input.clear("1234567890")

firstname_field = driver.find_element_by_id("input-tex")
firstname_input.clear()
firstname_input.clear("1234567890")

firstname_field = driver.find_element_by_id("input-company")
firstname_input.clear()
firstname_input.clear("CleverOnly")

firstname_field = driver.find_element_by_id("input-address-1")
firstname_input.clear()
firstname_input.clear("111 hollywood")

firstname_field = driver.find_element_by_id("input-address-2")
firstname_input.clear()
firstname_input.clear("lane1")

firstname_field = driver.find_element_by_id("input-city")
firstname_input.clear()
firstname_input.clear("Chicago")

firstname_field = driver.find_element_by_id("input-postcode")
firstname_input.clear()
firstname_input.clear("60000")

firstname_field = driver.find_element_by_id("input-password")
firstname_input.clear()
firstname_input.clear("12345")

firstname_field = driver.find_element_by_id("input-confirm")
firstname_input.clear()
firstname_input.clear("12345")

