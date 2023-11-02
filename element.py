from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep


driver=Chrome()
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()
driver.set_page_load_timeout(5)

body=driver.find_element(By.XPATH,'//body')
body.screenshot('body.png')


driver.find_element(By.TAG_NAME,'textarea').send_keys('amit')
sleep(2)

le=driver.find_elements(By.TAG_NAME,'textarea')
le[1].send_keys("ki")
le[1].screenshot('photo.png')
sleep(3)
