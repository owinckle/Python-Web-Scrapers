from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

WEBSITE		= "https://www.youtube.com/user/AllTrapNation" + "/videos"
CSV_FILE	= "yt-scraped.csv"

def main():
	source	= requests.get(WEBSITE).text
	soup	= BeautifulSoup(source, "lxml")
	search	= soup.find_all("div", class_="yt-lockup-content")

	titles	= []
	links	= []
	for elem in search:
		title	= elem.h3.text.split("-")[:-1]
		title	= "".join(title)
		titles.append(title)

		link	= elem.a["href"]
		link	= "https://www.youtube.com" + link
		links.append(link)

	titles		= np.array(titles)
	links		= np.array(links)
	df			= pd.DataFrame({"title": titles, "link":links})
	df.to_csv(CSV_FILE)

if __name__ == "__main__":
	main()