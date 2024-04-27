from selenium import webdriver
import time


AMZ_URL = "https://www.amazon.com.br/Panela-El%C3%A9trica-Arroz-Vidro-Titanium/dp/B0C6BRV2JS/ref=sr_1_1_sspa?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2AJTUE79MLAM4&dib=eyJ2IjoiMSJ9.hWP_dMfF2Sp97TEGmoPK0G38OwPre4SBNWSFzUVRRaG1YSLS0GMO0ImRHQ4NlbsoRQGza4ycVeASUvnwuyc_WLdDrqaT91IM7UgUYP6Yt677fKZmPAZXdKbKZFMSaJm56o8vcfLoAOrYezESsJT3jLier-R5uoBTXO-o7dtfSd8Hz3Dv4DgO51tTSRCzyU1AgEzbupK4p6U_mxsoJPm92XXW9RxSR_MTjzADWVkpOjbfMgTDhXpqKvDFiOgCfvXAL8_homzpsu_DeFcEgE5suGdo9j1pvXlkFcLCZMt7tE0.sAa8fmiU5RAnYwSne3CeUwtXZ2wzEwFxRMstJmyVSU0&dib_tag=se&keywords=panela+de+arroz+eletrica&qid=1709237777&sprefix=panela+de+arroz+eletri%2Caps%2C210&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
#manter chrome aberto
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(AMZ_URL)

time.sleep(10)

price_dollar = driver.find_element(by="class name", value="a-price-whole")
price_cents = driver.find_element(by="class name", value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

# driver.close() #fecha a guia
driver.quit() #fecha o navegador