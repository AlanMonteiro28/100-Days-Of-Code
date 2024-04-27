from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = "https://secure-retreat-92358.herokuapp.com/"
MY_EMAIL = "YOUR EMAIL"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

fname_input = driver.find_element(by="name", value="fName")
fname_input.send_keys("Alan")
sleep(1)
lname_input = driver.find_element(by="name", value="lName")
lname_input.send_keys("Monteiro")
sleep(1)
email_input = driver.find_element(by="name", value="email")
email_input.send_keys(MY_EMAIL)
sleep(1)
submit = driver.find_element(by="tag name", value="button")
submit.click()
sleep(5)
driver.quit()
