from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
import pandas as pd

options = Options()

driver = webdriver.Chrome(options=options)

def scr(url):
    driver.get(url)

    time.sleep(2)

    items = driver.find_elements(By.CLASS_NAME, "searchresultitem")

    item_name = []
    url_list = []
    # item_price = []
    stock_flg = []

    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, "[class*='title--']")
            item_name.append(title.text.strip())
        except NoSuchElementException:
            item_name.append("")

        link = item.find_element(By.TAG_NAME, "a")
        url_list.append(link.get_attribute("href"))

        # price = item.get_attribute("data-track-price")
        # item_price.append(price if price else "")

        text_lines = item.text.split("\n")

        if "売り切れ" in text_lines:
            stock_flg.append(1)
        else:
            stock_flg.append(0)

    df = pd.DataFrame([item_name, url_list, stock_flg]).T
    df.columns = ["item_name", "url", "stock_flg"]

    driver.quit()

    return df

def main():
    url = 'https://search.rakuten.co.jp/search/mall/anker/'
    df = scr(url)
    print(df)
    df.to_csv("practice/web_scraping/test.csv", index=False)

if __name__ == "__main__":
    main()