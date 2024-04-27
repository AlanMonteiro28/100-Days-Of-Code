from bs4 import BeautifulSoup
import requests

class WebScrapper:
    def __init__(self, url):
        self.url = url
        self.soup = self.create_soup()

    def create_soup(self):
        self.zillowc_r = requests.get(self.url)
        self.zillowc_r.raise_for_status()
        self.zillowc_data = self.zillowc_r.content
        return BeautifulSoup(self.zillowc_data, "html.parser")
    
    def get_prices(self):
        #PropertyCardWrapper__StyledPriceLine
        price_element = self.soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
        self.all_prices = [price.text.split("+")[0] if "+" in price.text else price.text.split("/mo")[0] for price in price_element]
        return self.all_prices
    
    def get_address(self):
        #StyledPropertyCardDataArea-anchor
        address_element = self.soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
        self.all_adress = [adress.text.strip() for adress in address_element]
        return self.all_adress
    
    def get_links(self):
        #StyledPropertyCardPhotoBody
        link_element = self.soup.find_all("div", class_="StyledPropertyCardPhotoBody")
        self.all_links = [link.a["href"] for link in link_element]
        return self.all_links
