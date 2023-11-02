from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep

driver=Chrome()
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")
sleep(2)

ele=driver.find_element(By.ID,"confirm")
#driver.execute_script("arguments[0].scrollIntoView();",ele)
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.execute_script("window.scrollBy(0,400)")
driver.find_element(By.ID,"prompt").click()
alert=Alert(driver)
sleep(2)
alert.send_keys('amit')
sleep(2)
alert.accept()



sleep(3)
