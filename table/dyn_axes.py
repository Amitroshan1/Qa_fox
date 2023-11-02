from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver=Chrome()
driver.maximize_window()
driver.get("https://demo.opencart.com/admin/index.php?route=common/login")
sleep(3)

driver.find_element(By.ID,"input-username").send_keys("demo")
driver.find_element(By.ID,"input-password").send_keys("demo")
driver.find_element(By.XPATH,"//button[@type='submit']").click()


wait= WebDriverWait(driver,10)
ele=wait.until(ec.visibility_of_element_located((By.XPATH,"//button[@data-bs-dismiss='modal']")))
ele.click()

#driver.find_element(By.XPATH,"//a[contains(text(),'Sales')]").click()
driver.find_element(By.LINK_TEXT,"Sales").click()
driver.find_element(By.LINK_TEXT,"Orders").click()



cust_name="hasan zein"
driver.find_elements(By.XPATH,"//form[@id='form-order']//tr//td[text()='"+cust_name+"']")
sleep(3)

driver.find_element(By.XPATH,"//form[@id='form-order']//tr//td[text()='"+cust_name+"']/preceding-sibling::td[3]/input[@type='checkbox']").click()

sleep(3)