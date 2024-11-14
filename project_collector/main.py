# 데이터를 수집할 수 있는 웹사이트 개발!
#  1. 화면: 특정 정보 입력(streamlit)
#  2. 수집: 데이터 수집(requests, beautifulsoup)
#  3. 화면: 출력, 엑셀 다운로드(streamlit, pandas)
#  4. 저장: 데이터베이스 저장(pymysql + MariaDB)
from fnc_service import collect_news

category = "digital" #IT

def main():
    print("Start collector")
    collect_news(category)

if __name__ == "__main__":
    main()