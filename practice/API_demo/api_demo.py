import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from slack_sdk import WebClient
from dotenv import load_dotenv
from pathlib import Path

import time
import pandas as pd
import datetime


options = Options()

driver = webdriver.Chrome(options=options)

def scr(url):
    driver.get(url)

    time.sleep(2)

    item_name = []
    url_list = []
    # item_price = []
    stock_flg = []

    items = driver.find_elements(By.CLASS_NAME, "searchresultitem")

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

def slack_bot(df):
    load_dotenv()
    token = os.environ["SLACK_BOT_TOKEN"]
    channel = os.environ["CHANNEL_ID"]

    df = df.sort_values(by="stock_flg", ascending=False)

    script_dir = Path(__file__).resolve().parent
    csv_path = script_dir / "test.csv"
    df.to_csv(csv_path, index=False)

    today = datetime.date.today()
    out_of_stock_rate = df.stock_flg.sum() / len(df)

    client = WebClient(token=token)

    # 1) 概要メッセージを送信
    summary = (
        f"楽天の在庫情報です。欠品率は{out_of_stock_rate:.1%}です。\n"
        f"件数: {len(df)}件（売り切れ: {int(df.stock_flg.sum())}件）"
    )
    client.chat_postMessage(channel=channel, text=summary)

    # 2) CSV の中身をメッセージで送信
    with open(csv_path, "r", encoding="utf-8") as f:
        csv_content = f.read()

    if len(csv_content) <= 3900:
        client.chat_postMessage(
            channel=channel,
            text=f"```\n{csv_content}\n```",
        )
    else:
        client.chat_postMessage(
            channel=channel,
            text=f"```\n{csv_content[:3900]}\n```",
        )

def main():
    url = 'https://search.rakuten.co.jp/search/mall/anker/'
    df = scr(url)
    print(df)
    slack_bot(df)

if __name__ == "__main__":
    main()