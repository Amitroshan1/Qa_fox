from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep


driver=Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)

driver.find_element(By.ID,"datepicker").click()
sleep(1)
mon="June"
yr="2022"
dt="5"

while True:
    month=driver.find_element(By.CSS_SELECTOR,'span.ui-datepicker-month').text
    year=driver.find_element(By.CSS_SELECTOR,'span.ui-datepicker-year').text
    

    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.CSS_SELECTOR,"span.ui-icon-circle-triangle-w").click()
date= driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for item in date:
    if item.text==dt:
        item.click()

sleep(3)



