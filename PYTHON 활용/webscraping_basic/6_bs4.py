import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status() # 문제 생기면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml") # 가져온 res.text 정보를 lxml를 통해서 Beautifulsoup 객체로 변환 

# print(soup.title) # soup 객체에서 처음 발견되는 title element를 반환 
# print(soup.title.get_text()) # 가져온 정보중 text만 출력

# print(soup.a) # soup 객체에서 처음 발견되는 a element를 반환 
# print(soup.a.get_text())
# print(soup.a.attrs) # a element 의 속성 정보를 출력
# print(soup.a["href"]) # a element 의 href의 속성 값을 가져온다.

# 잘 모르는 페이지일 경우 찾는법
# print(soup.find("a", attrs = {"class":"Nbtn_upload"})) # class = "Nbtn_upload" 인 a element 를 찾아줘 = 가져온 soup 정보중 처음으로 발견되는 a 태그에서 class가 "Nbtn_upload"인 element의 속성을 출력
# print(soup.find("div", attrs = {"class":"Nbtn_upload"})) # class = "Nbtn_upload" 인 div element 를 찾아줘
# print(soup.find("li", attrs = {"class":"rank01"}))
rank1 = soup.find("li", attrs = {"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling) # .next_sibling : 위에서 찾은 elemet = rank1 의 다음 element를 출력
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # .previous_sibling : .next_sibling의 역순
# print(rank2.a.get_text())
# print(rank1.parent) # 부모인차 출력 


# rank2 = rank1.find_next_sibling("li") # rank1 다음 중 li인 것만 찾는다
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li") # rank2 다음 중 li인 것만 찾는다
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li") # rank3 이전 중 li인 것만 찾는다
# print(rank2.a.get_text())


# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="프리드로우-제394화 태준 그룹 (9)") # a태그의 내용중 text가 "프리드로우-제394화 태준 그룹 (9)" 인 a태그의 모든 정보 가져오기
print(webtoon)