from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Create Firefox options to accept insecure certificates and ignore certificate errors
options = Options()
options.accept_insecure_certs = True

# Specify the path to the geckodriver executable if not in the system PATH
driver = webdriver.Firefox(options=options)

# Navigate to a website with SSL certificate issues

# Continue with your test automation


driver.get("https://expired.badssl.com/")


print(driver.page_source)