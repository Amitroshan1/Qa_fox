from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep


driver=Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")


driver.execute_script("window.scrollBy(0,1200)")
row=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
sleep(1)
col= driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th")
sleep(1)

for r in range(2,len(row)+1):
    for c in range(1,len(col)+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+ str(r)+"]/td["+str(c)+"]")
        print(data.text,end=' ')
        
    print()

sleep(5)