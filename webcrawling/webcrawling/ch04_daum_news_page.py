import requests
from bs4 import BeautifulSoup
from fnc_news import get_news_info

# URL 주소
#   - https -> 프로토콜 
#   - news.daum.net/~~~ -> 도메인 주소
#   - ?page=1           -> 쿼리스트링
#                          (서버에 데이터를 전달할 떄 사용)

page = 1
count = 1
while True:
    url = f"https://news.daum.net/breakingnews/digital?page={page}"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    link_list = doc.select("ul.list_news2 a.link_txt")
    
    # 뉴스기사 마지막 페이지 체크
    if len(link_list) == 0:
        break

    for  link in link_list:
        print(f"{count+1} ================================================================")
        get_news_info(link["href"])
        count+=1
    page+=1
    
    

        