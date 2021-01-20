import requests
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


uClient = uReq('https://lol.gamepedia.com/Category:Champion_Square_Images')
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

cells = page_soup.findAll("li",{"class":"gallerybox"})
nome = ''
for cell in cells:
	nome = cell.div.div.a.img["alt"]
	nome =  nome.replace("Square", "")
	if(nome.find('Unreleased') == -1): 
		with open(nome, "wb") as f:
        		f.write(requests.get(cell.div.div.a.img['src']).content)
        		f.close()
