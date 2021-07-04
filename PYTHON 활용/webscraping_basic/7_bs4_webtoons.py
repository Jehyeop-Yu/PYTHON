import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() # 문제 생기면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml") # 가져온 res.text 정보를 lxml를 통해서 Beautifulsoup 객체로 변환 

# 네이버 웹툰 전체 목록 가져오기 
cartoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title 인 모든 "a" element 를 반환
for cartoon in cartoons:
    print(cartoon.get_text())