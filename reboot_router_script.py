from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.get("http://192.168.1.1/")
pwd = driver.find_element_by_id("INPUT_Psd")
pwd.clear() #cleared any data that was pre filled
pwd.send_keys("admin") #entered the pass
pwd.send_keys(Keys.RETURN) #pressed enter

driver.get("http://192.168.1.1/cgi-bin/webproc?getpage=html/index.html&var:menu=maintenance&var:page=system") #go to the wireless page

rebootbtn = driver.find_element_by_id("reboot123") # select the submit button to apply changes
rebootbtn.click() # click the Apply button to make changes
driver.close()

