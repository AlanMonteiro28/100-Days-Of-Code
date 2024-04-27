from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

article_count = driver.find_element(by="css selector", value=('[title="Special:Statistics"]'))
#article_count.click()

all_portals = driver.find_element(by="link text", value="Content portals")
#all_portals.click()

search = driver.find_element(by="name", value="search")
search.send_keys("Python", Keys.ENTER)

driver.quit()

