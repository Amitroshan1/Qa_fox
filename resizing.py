from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains,Keys

driver=Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

sleep(2)

ele=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")

chain=ActionChains(driver)

chain.drag_and_drop_by_offset(ele,10,15).perform()
sleep(2)