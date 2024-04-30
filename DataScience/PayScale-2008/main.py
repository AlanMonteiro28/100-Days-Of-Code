from selenium import webdriver
from time import sleep

school_name = "Finance"
URL = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
sleep(10)
search = driver.find_element(by="xpath", value='//*[@id="__next"]/div/div[1]/article/div[1]/div/input')
search.send_keys(school_name)
sleep(5)
rows = driver.find_elements(by="class name", value="data-table__row")
for row in rows:
    major_element = row.find_element(by="class name", value="csr-col--school-name")
    major = major_element.find_element(by="class name", value="data-table__value")
    if major.text == school_name:
        # rank
        rank_element = row.find_element(by="class name", value="csr-col--rank")
        rank = rank_element.find_element(by="class name", value="data-table__value").text
        # early and mid career pay
        pay_elements = row.find_elements(by="class name", value="csr-col--right")
        # early
        early_pay = pay_elements[0].find_element(by="class name", value="data-table__value").text
        # mid
        mid_pay = pay_elements[1].find_element(by="class name", value="data-table__value").text

        print(f"Rank: {rank}\nMajor: {major.text}\nEarly Career Pay: {early_pay}\nMid Career Pay: {mid_pay}")

driver.quit()
