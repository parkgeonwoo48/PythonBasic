import requests
from bs4 import BeautifulSoup
from fnc_news import get_news_info

url = "https://news.daum.net/breakingnews/digital"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

link_list = doc.select("ul.list_news2 a.link_txt")

for i, link in enumerate(link_list):
    print(f"{i+1} ================================================================")
    get_news_info(link["href"])
    