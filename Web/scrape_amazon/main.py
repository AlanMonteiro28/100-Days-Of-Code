from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = "YOUR GMAIL ACCOUNT"
MY_PASS = "YOUR PASSWORD"

BUY_PRICE = 500

AMZ_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Sec-Ch-Ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "YOUR USER-AGENT",
  }

AMZ_URL = "https://www.amazon.com.br/Panela-El%C3%A9trica-Arroz-Vidro-Titanium/dp/B0C6BRV2JS/ref=sr_1_1_sspa?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2AJTUE79MLAM4&dib=eyJ2IjoiMSJ9.hWP_dMfF2Sp97TEGmoPK0G38OwPre4SBNWSFzUVRRaG1YSLS0GMO0ImRHQ4NlbsoRQGza4ycVeASUvnwuyc_WLdDrqaT91IM7UgUYP6Yt677fKZmPAZXdKbKZFMSaJm56o8vcfLoAOrYezESsJT3jLier-R5uoBTXO-o7dtfSd8Hz3Dv4DgO51tTSRCzyU1AgEzbupK4p6U_mxsoJPm92XXW9RxSR_MTjzADWVkpOjbfMgTDhXpqKvDFiOgCfvXAL8_homzpsu_DeFcEgE5suGdo9j1pvXlkFcLCZMt7tE0.sAa8fmiU5RAnYwSne3CeUwtXZ2wzEwFxRMstJmyVSU0&dib_tag=se&keywords=panela+de+arroz+eletrica&qid=1709237777&sprefix=panela+de+arroz+eletri%2Caps%2C210&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

r = requests.get(url=AMZ_URL, headers=AMZ_HEADERS)
r.raise_for_status()
amz_web_page = r.text

soup = BeautifulSoup(amz_web_page, "html.parser")

prod_title = soup.find(id="productTitle").getText().strip()
price_whole = soup.find(name='span', class_="a-price-whole").getText().strip(",")
price_fraction = soup.find(name='span', class_="a-price-fraction").getText()

print(prod_title)
print(price_whole)
print(price_fraction)

price = float(f"{price_whole}.{price_fraction}")
print(price)

if price < BUY_PRICE:
    message = f"{prod_title} is cheaper now!\nCurrent price: R$ {price}\nTake advantage of the offer:\n{AMZ_URL}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:AMAZON PRICE ALERT!!\n\n{message}".encode("utf-8"))