# SELENIUM
#  - 설치: pip install selenium
#  - 웹 크롤링(정적, 동적 모두 가능) + 자동화
#      ㄴ SELENIUM이 제어할 수 있는 웹 브라우저 사용
#  - 과거에 웹브라우저 테스트 도구!

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 디폴트: SELENIUM 코드 종료 -> 웹브라우저 종료
# 1. 셀레니움 웹브라우저 설정
options = Options()
options.add_experimental_option("detach",True) # 웹브라우저 종료x
# options.add_argument("headless") # 셀레니움이 백그라운드 동작(개발완려)

# ※ 셀레니움이 로봇이 아닌척 하는 방법
options.add_argument("disable-blink-features=AutomationControlled")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])



# ※ 셀레니움 4버전 이하에서는 ChromeDriver를 설치해서 사용!
#    4버전부터는 설치할 필요 없음!
#    service = Service(ChromDriverManager().install())

# 2. 셀레니움 웹브라우저 생성
driver = webdriver.Chrome(options=options)
# 3. 셀레니움 웹브라우저 사용
driver.get("https://www.naver.com")
time.sleep(5)
print(driver.page_source) # -> 네이버 메인 페이지 소스코드

search = driver.find_element(By.ID, "query")
search.send_keys("정우성")
search.send_keys(Keys.ENTER)
time.sleep(5)

# 현재 웹브라우저 페이지의 소스코드 GET
print(driver.page_source) # -> 정우성 검색 네이버 페이지 소스코드

# + BeautifulSoup
