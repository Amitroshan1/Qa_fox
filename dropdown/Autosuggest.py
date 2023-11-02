from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains,Keys


driver=Chrome()
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
sleep(2)

driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()
sleep(2)

driver.find_element(By.ID,"fromCity").send_keys('g')
sleep(2)
chain=ActionChains(driver)

chain.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
sleep(2)