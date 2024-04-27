from selenium import webdriver
from web_scraper import WebScrapper
from time import sleep

#WebScrapper use -> get_prices // get_adress // get_links

ZILOWC_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORMS_URL = "YOUR FORMS URL"

#scraping informations
zillowc_data = WebScrapper(url=ZILOWC_URL)
prices = zillowc_data.get_prices()
address = zillowc_data.get_address()
links = zillowc_data.get_links()

#open and fill out form
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORMS_URL)
sleep(2)

for i in range(len(address)):
    address_input = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    address_input.send_keys(address[i])
    sleep(1)
    price_input.send_keys(prices[i])
    sleep(1)
    link_input.send_keys(links[i])
    sleep(1)
    submit_button.click()
    sleep(1)
    driver.refresh()
    sleep(2)

driver.quit()

