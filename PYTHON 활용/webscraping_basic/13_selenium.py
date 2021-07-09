from selenium import webdriver

browser = webdriver.Chrome("F:/코딩/PYTHON/PYTHON 활용/webscraping_basic/chromedriver.exe")
browser.get("http://naver.com")

# TERMINAL 명령
from selenium import webdriver
browser = webdriver.Chrome("F:/코딩/PYTHON/PYTHON 활용/webscraping_basic/chromedriver.exe")
browser.get("http://naver.com")
elem = browser.find_element_by_class_name("link_login") # 로그인 버튼 찾기 
elem.Click() # 버튼 누르기 
browser.back() # 뒤로가기
browser.forward() # 앞으로 가기
browser.refresh() # 새로고침
# 검색창 찾기 및 사용
elem = browser.find_element_by_id("query")
from selenium.webdriver.common.keys import Keys
elem.send_keys("입력할 문장적기") # 검색창 입력
elem.send_keys(Keys.ENTER) # 검색 엔터

# 태그로 정보 가져오기
elem = browser.find_elements_by_tag_name("a") # 태그 네임으로 "a"태그 엘리먼트들 다 가져오기
for e in elem: # 위 여러 엘리먼트중에 "href" 엘리먼트 가져오기
    elem.get_attribute("href")

# 다음웹 으로 이동
browser.get("http://daum.net")
