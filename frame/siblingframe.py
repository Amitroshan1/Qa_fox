from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from time import sleep



opt=options.Options()
opt.add_argument('--headless=True')

driver=Chrome(opt)
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()
sleep(2)

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
left=driver.find_element(By.XPATH,"//body").text
print(left)
driver.switch_to.parent_frame()
driver.switch_to.frame("frame-middle")
middel=driver.find_element(By.XPATH,'//body').text
print(middel)
driver.switch_to.parent_frame()
driver.switch_to.frame("frame-right")
right=driver.find_element(By.XPATH,"//body").text
print(right)
