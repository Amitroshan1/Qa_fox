from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains,Keys

driver=Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

driver.find_element(By.ID,'input-firstname').send_keys("amit")
chain=ActionChains(driver)
chain.send_keys(Keys.TAB).pause(3).send_keys('kumar')\
.send_keys(Keys.TAB).pause(3).send_keys('aaa@gmail.com')\
.send_keys(Keys.TAB).pause(3).send_keys('8210178454')\
.send_keys(Keys.TAB).pause(3).send_keys("1245")\
.send_keys(Keys.TAB).pause(3).send_keys("1245")\
.send_keys(Keys.TAB).pause(3).perform()
radio=driver.find_elements(By.XPATH,"//input[@name='newsletter']")
radio[0].click()
chain.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.SPACE).pause(2)\
.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
sleep(3)
