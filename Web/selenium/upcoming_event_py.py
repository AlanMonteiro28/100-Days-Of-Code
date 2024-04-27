from selenium import webdriver

URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

upcoming_events = {}
for i in range(1, 6):
    datetime_element = driver.find_element(by="xpath", value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
    datetime_value = datetime_element.get_attribute("datetime").split("T")[0]
    anchor_value = driver.find_element(by="xpath", value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a').text
    upcoming_events[i-1] = {"time":datetime_value,
                          "name":anchor_value,}
    
print(upcoming_events)



driver.quit()