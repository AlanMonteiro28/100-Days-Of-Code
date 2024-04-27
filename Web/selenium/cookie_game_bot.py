from selenium import webdriver
import time

URL = "https://orteil.dashnet.org/cookieclicker/"

verification_time = time.time() + 5
run_game_time = time.time() + (5*60)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(1)
lang_select = driver.find_element(by="id",value="langSelect-EN")
lang_click = lang_select.click()
time.sleep(1)

def buy_item():
    all_elements_enabled = driver.find_elements(by="class name", value="unlocked")
    if all_elements_enabled:
        return all_elements_enabled[-1].click()
    else:
        return None
    
cookie_element = driver.find_element(by="id", value="bigCookie")
#time_test = time.time() + 15
while True:
    cookie_element.click()
    if time.time() >= verification_time:
        buy_item()
        verification_time = time.time() + 5
    
    if time.time() > run_game_time:
        cookie_per_second = driver.find_element(by="id", value="cookiesPerSecond")
        print(f'Cookies per second: {cookie_per_second.text.split(":")[1]}')
        break
