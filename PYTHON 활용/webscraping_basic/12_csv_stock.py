# 네이버 코스피 시가총액 순위 정보 가져오기 
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액 1-200.cvs"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title ="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# ["N", "종목명", "현재가", ...]
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_raws = soup.find("table", attrs = {"class":"type_2"}).find("tbody").find_all("tr")
    for raw in data_raws:
        columns = raw.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 skip = 공백지우기 line:22 .strip()추가
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)