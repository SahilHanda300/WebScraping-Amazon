import requests
from bs4 import BeautifulSoup
import pandas as pd



# Taking Input for Search Query

name = input("Enter Search Query : ")



# Headers used for preventing Server Error
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(f"https://www.amazon.in/s?k={name}&crid=2K4C4LAIP0K9O&sprefix=samsu%2Caps%2C192&ref=nb_sb_ss_ts-doa-p_2_5",headers=headers)

soup = BeautifulSoup(r.text,"html.parser")

title = soup.select("span.a-size-medium.a-color-base.a-text-normal")

price = soup.select("span.a-price-whole")


data={"Product":[],"Price":[]}


# It will show the top 10 recommendations of Title
# and Product by following an incrementer from the
# top :)


title_length=0
for titles in title:
    title_length+=1
    data["Product"].append(titles.string)
    if title_length==10:
        break


price_length = 0
for prices in price:
    price_length+=1
    data["Price"].append(prices.string)
    if price_length==10:
        break

df = pd.DataFrame.from_dict(data)

df.to_csv("ScrapedData.csv",index=False)


# The Data generated in .csv right now is generated as per
# date of 08-10-2023
