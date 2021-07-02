import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status() # 문제 생기면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml") # 가져온 res.text 정보를 lxml를 통해서 Beautifulsoup 객체로 변환 
print(soup.title)