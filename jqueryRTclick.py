from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains,Keys

driver=Chrome()
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
 

button=driver.find_element(By.XPATH,"//span[text()='right click me']")

chain=ActionChains(driver)
chain.context_click(button).perform()
sleep(2)
quit=driver.find_element(By.XPATH,"//li/span[text()='Quit']")
chain.click(quit).perform()
sleep(2)

driver.switch_to.alert.accept()

sleep(2)



