import requests
# res = requests.get("http://naver.com")
# # res = requests.get("http://nadocoding.tistory.com")
# print("응답코드 :", res.status_code) # 200 이면 정상

# # if res.status_code == requests.codes.ok: # requests.codes.ok == 200
# #     print("정상입니다.")
# # else:
# #     print("문제가 생겼습니다. [에러코드", res.status_code, "]")

# res.raise_for_status() # 올바르게 html코드를 가져오면 문제없음
# print("웹 스크래핑을 진행합니다.")


# 기본적으로 사용하는 방법, 습관적으로 해야하는 과정 : 스크래핑이 가능한지 확인
res = requests.get("http://google.com") 
res.raise_for_status()

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)