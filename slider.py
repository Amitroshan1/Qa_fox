from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver=Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)

ele=driver.find_element(By.ID,"slider")

chain=ActionChains(driver)
chain.drag_and_drop_by_offset(ele,100,0).perform()
sleep(2)
chain.click_and_hold