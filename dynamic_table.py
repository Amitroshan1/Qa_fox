from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import options
from time import sleep


driver=Chrome()
driver.get('https://www.python.org/')
driver.maximize_window()
driver.implicitly_wait(5)
sleep(2)

chain=ActionChains(driver)
ele1=driver.find_element(By.XPATH,"//li[@id='about']/a")
ele2=driver.find_element(By.LINK_TEXT,"Applications")

chain.move_to_element(ele1).move_to_element(ele2).click().perform()
sleep(2)
driver.switch_to.new_window("tab")
driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
driver.execute_script("window.scrollBy(0,500)")
db=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction1()']")

chain.double_click(db).perform()
sleep(2)

src=driver.find_element(By.ID,"draggable")
dest=driver.find_element(By.ID,"droppable")
chain.drag_and_drop(src,dest).perform()
sleep(2)
driver.close()