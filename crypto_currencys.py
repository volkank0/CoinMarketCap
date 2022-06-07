from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://coinmarketcap.com/")

CRYPTO_CURRENCYS = "//*[@id='__next']/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr"
CRYPTO_CURRENCY_NAME_XPATH = CRYPTO_CURRENCYS + "[{}]/td[3]/div/a/div/div/p"
CRYPTO_CURRENCY_PRICE_XPATH = CRYPTO_CURRENCYS + "[{}]/td[4]/div/a/span"
CRYPTO_CURRENCY_MARKET_CAP = CRYPTO_CURRENCYS + "[{}]/td[7]/p/span[2]"
CRYPTO_CURRENCY_CIRCULATING_SUPPLY = CRYPTO_CURRENCYS + "[{}]/td[9]/div/div/p"

countCurrency = len(driver.find_elements(By.XPATH, CRYPTO_CURRENCYS))
for counter in range(1, countCurrency + 1):
    if counter <= countCurrency:
        CURRENCY_NAME = driver.find_element(
            By.XPATH, CRYPTO_CURRENCY_NAME_XPATH.format(counter))
        WRITE_CURRENCY_NAME = CURRENCY_NAME.text
        CURRENCY_PRICE = driver.find_element(
            By.XPATH, CRYPTO_CURRENCY_PRICE_XPATH.format(counter)).text
        CURRENCY_MARKET_CAP = driver.find_element(
            By.XPATH, CRYPTO_CURRENCY_MARKET_CAP.format(counter)).text
        CURRENCY_CIRCULATING_SUPPLY = driver.find_element(
            By.XPATH, CRYPTO_CURRENCY_CIRCULATING_SUPPLY.format(counter)).text

        ActionChains(driver).move_to_element(CURRENCY_NAME).perform()

        with open("crcny_log.csv", mode="a+", encoding="utf-8") as log:
            log.write("{name} ; Anlık Fiyatı: {price}; Piyasa Değeri: {market}; Dolaşımdaki Arz: {supply}".format(
                name=WRITE_CURRENCY_NAME, price=CURRENCY_PRICE, market=CURRENCY_MARKET_CAP, supply=CURRENCY_CIRCULATING_SUPPLY) + "\n")

driver.close()
