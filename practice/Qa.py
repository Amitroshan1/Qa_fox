from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver=Chrome()
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")
sleep(2)


list_box=driver.find_element(By.XPATH,"//*[@id='HTML1']/preceding-sibling::div[@id='HTML14']//select")
list_box.send_keys('Volvo')
sleep(2)
opt=Select(list_box)
opt.select_by_visible_text('Hyundai')
sleep(2)


dropdown=driver.find_element(By.XPATH,"//*[@id='HTML1']/descendant::select")
dropdown.send_keys('doc 3')
sleep(2)
opt=Select(dropdown)
opt.select_by_index(2)
sleep(3)