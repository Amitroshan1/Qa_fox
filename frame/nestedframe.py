from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

driver=Chrome()
driver.get("https://letcode.in/frame")
driver.maximize_window()
driver.implicitly_wait(5)


driver.switch_to.frame("firstFr")
sleep(1)
driver.find_element(By.XPATH,"//input[@name='fname']").send_keys("Amit")
sleep(1)
driver.find_element(By.XPATH,"//input[@name='lname']").send_keys("Kumar")
sleep(1)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

child=driver.find_element(By.XPATH,"//iframe[@class='has-background-white']")

driver.switch_to.frame(child)
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("amit@gamil.com")

driver.switch_to.parent_frame()
sleep(1)
driver.find_element(By.XPATH,"//input[@name='lname']").clear()


sleep(3)