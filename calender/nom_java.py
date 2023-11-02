from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep


driver=Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)

#driver.execute_script("document.getElementById('datepicker').value='06/01/2023'")

driver.find_element(By.ID,"datepicker").send_keys("06/01/2023")
sleep(3)
