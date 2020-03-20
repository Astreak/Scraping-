import requests 
import pprint
import html5lib
from bs4  import BeautifulSoup
import re
import pandas  as pd
import csv
import numpy as np

link=f"https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=on&page=7"
def get_html_script(link,filename_with_extension):
	data=requests.get(link)
	soup=BeautifulSoup(data.content,"html5lib")
	with open(filename_with_extension,"w") as file:
		file.write(str(soup))
	return soup
	#_1vC4OE
	#_3liAhj
data=get_html_script(link,"scraping.html")
l=[]
for i in data.find_all("a"):
	if i.get("href").startswith("https"):
			l.append(i.get("href"))
products=[]
ratings=[]
price=[]
for j in data.find_all("a",class_="_2cLu-l"):
	products.append(j.get("title"))


for u in data.find_all("div",attrs={"class":"_3liAhj"}):
	k=u.find("div",attrs={"class":"_1vC4OE"})

	r=u.find("div",attrs={"class":"hGSR34"})
	price.append(k.get_text())
	if r==None:
			ratings.append(float(0))
	else:
		ratings.append(float(r.get_text()))

deliop=products[0][0]
for h in range(len(price)):
	price[h]=re.sub("[^1-9]","",price[h])


products=np.array(products)
price=np.array(price)
ratings=np.array(ratings)
biggy=pd.DataFrame({"PRODUCTS":products,"RATINGS":ratings,"PRICE":price})
csv_file=biggy.to_csv(f"SCRAPED_FLIPKART_IPHONE7.csv",sep=",")







