from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
import utils


driver=Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
sleep(2)

path="C:\\Users\\dell\\Downloads\\xlsheet.xlsx"
sheetname="Sheet2"
row=utils.row(path,sheetname)
print(row)

for data in range(1,row):
    user=utils.read_data(path,sheetname,data,1)
    print(user)
    passwor=utils.read_data(path,sheetname,data,2)
    print(passwor)

    username=driver.find_element(By.ID,"Email")
    username.clear()
    username.send_keys(user)
    sleep(2)
    password=driver.find_element(By.ID,"Password")
    password.clear()
    password.send_keys(passwor)
    sleep(2)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    if driver.title == 'Dashboard / nopCommerce administration':
        print('logged in')
        driver.find_element(By.LINK_TEXT,"Logout").click()
        sleep(2)
    else:
        driver.save_screenshot(".//photo.png")
        print('not logged in')
        sleep(2)



