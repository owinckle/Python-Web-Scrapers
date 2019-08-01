import requests
from bs4 import BeautifulSoup

URL		= "https://www.amazon.fr/ASUS-GeForce-Overclocked-Graphics-ROG-STRIX-RTX-2080-O11G/dp/B07HY6QWXN/ref=sr_1_2?crid=9UHGMHY2IK20&keywords=rtx+2080+ti&qid=1564639065&s=gateway&sprefix=rtx%2Caps%2C207&sr=8-2"

def main():
	page	= requests.get(URL).text
	soup	= BeautifulSoup(page, "lxml")

	title	= soup.find(id="productTitle").text
	price	= soup.find(class_="a-offscreen").text
	print("Item: " + title.strip())
	print("Price: " + price.strip())

if __name__ == "__main__":
	main()