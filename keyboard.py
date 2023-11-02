from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

driver=Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
sleep(2)

driver.find_element(By.ID,"input-email").send_keys("amit@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("1234")

#driver.find_element(By.ID,"input-password").send_keys(Keys.ENTER)


# using Actionclass

chain=ActionChains(driver)
chain.send_keys(Keys.ENTER).perform()
sleep(2)
expected=driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text

print(expected)
if expected == "Warning: No match for E-Mail Address and/or Password.":
    print('key action perfromed')
else:
    print('not performed')

sleep(2)
