# -*- coding: utf-8 -*-
"""Amazon_customer_Rating.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EHB-7LDLuti-sKOK1HLC2iNTFekEqBxx
"""

import requests
from bs4 import BeautifulSoup
print('✔️ Libraries imported successfully!')
link = 'https://www.amazon.in/Apple-iPhone-Pro-128GB-Silver/product-reviews/B0BDJPYT2J/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
r = requests.get(link)

soup = BeautifulSoup(r.content, 'html.parser')

names = soup.find_all('span', class_='a-profile-name')

names

cust_name = []
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())
cust_name

title = soup.find_all('a',class_='review-title-content')
title

review_title = []
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title

review_title[:] = [titles.lstrip('\n') for titles in review_title]
review_title

review_title[:] = [titles.rstrip('\n') for titles in review_title]
review_title

rating = soup.find_all('i',class_='review-rating')
rating

rate = []
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate

review = soup.find_all("span",{"data-hook":"review-body"})
review

review_content = []
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
review_content

review_content[:] = [reviews.lstrip('\n') for reviews in review_content]
review_content

review_content[:] = [reviews.rstrip('\n') for reviews in review_content]
review_content

len(cust_name)

cust_name.pop(0)

len(review_content)

len(rate)

rate.pop(0)

len(review_title)

import pandas as pd

df = pd.DataFrame()
df

df["Customer Name"] = cust_name
df

df['Rating'] = rate
df['Review Title'] = review_title
df['Review content'] = review_content
df