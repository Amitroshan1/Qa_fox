from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

driver=Chrome()
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")
sleep(2)

links= driver.find_elements(By.XPATH,"//div[@class='widget-content']/ul/li/a")
sleep(1)

for link in links:
    chain=ActionChains(driver)
    chain.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    sleep(2)
