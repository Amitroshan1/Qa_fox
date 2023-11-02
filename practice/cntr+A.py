from selenium.webdriver import Chrome,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=Chrome()
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")
sleep(2)

textarea=driver.find_element(By.XPATH,"//*[@id='HTML11']/child::div/textarea")
textarea.click()

#for clicking CTRL+A
textarea.send_keys(Keys.CONTROL,"a")
textarea.send_keys(Keys.BACKSPACE)

sleep(3)
textarea.send_keys(Keys.CONTROL,"z")

#using actionchain class
