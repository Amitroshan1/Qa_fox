from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


driver=Chrome()
driver.get("https://docs.oracle.com/javase/8/docs/api/")
driver.maximize_window()
driver.implicitly_wait(5)

# switching into frame
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"java.applet").click()

# Switching out of frame
driver.switch_to.default_content()
sleep(1)

# Refrse page for previous content
driver.refresh()

# switching into frame again
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"AbstractCellEditor").click()
sleep(1)
# Switching out of frame
driver.switch_to.default_content()
driver.refresh()
sleep(1)

# Using webelement
link=driver.find_element(By.XPATH,"//frame[@title='Package, class and interface descriptions']")
# switching into frame using wbelement
driver.switch_to.frame(link)
driver.find_element(By.LINK_TEXT,"compact1").click()
sleep(3)


