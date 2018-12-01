import webbrowser
from selenium import webdriver
import time

url = "file:///Users/srinivas/html_proj/html/index.html"
webbrowser.open(url)

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get(url)

print(driver.current_url)

var =  driver.find_element_by_class_name('form-control')
time.sleep(30)
print(var.getAttribute("value"))

# time.sleep(10)

driver.quit()       
