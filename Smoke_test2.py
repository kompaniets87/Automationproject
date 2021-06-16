from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
# to start Firefox use the line below
#driver = webdriver.Firefox(executable_path='driver/geckodriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()


wd_wait = WebDriverWait(driver, 10)
logo = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@title='Brainbucket']")))

new_registrant_btn = wd_wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Continue')]")))
new_registrant_btn.click()
new_registrant_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Continue')]")))