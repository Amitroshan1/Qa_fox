from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

driver=Chrome()
driver.maximize_window()
driver.get("https://demo.opencart.com/admin/index.php?route=common/login")
driver.implicitly_wait(5)
src=driver.page_source
print(type(src))


s='amit'
