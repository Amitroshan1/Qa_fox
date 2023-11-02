from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

driver=Chrome()
driver.maximize_window()
driver.get("https://demo.opencart.com/admin/index.php?route=common/login")
driver.implicitly_wait(5)

driver.find_element(By.ID,"input-username").send_keys('demo')
driver.find_element(By.ID,"input-password").send_keys('demo')
driver.find_element(By.XPATH,"//button[@type='submit']").click()

wait=WebDriverWait(driver,5)
cancle=wait.until(ec.visibility_of_element_located((By.XPATH,"//button[@type='button' and @data-bs-dismiss='modal']")))
cancle.click()

driver.find_element(By.LINK_TEXT,"Sales").click()
driver.find_element(By.LINK_TEXT,"Orders").click()

page_count=driver.find_elements(By.XPATH,"//div[@class='col-sm-6 text-start']//li")


for page in range(1,len(page_count)+1):
    pag=driver.find_element(By.XPATH,"//li[contains(@class,'active')]/span/following::a[1]")
    pag.click()
    print('pag clicked')
    sleep(3)
    
    


sleep(3)

