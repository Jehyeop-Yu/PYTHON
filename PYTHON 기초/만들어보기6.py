# 사전
cabinet = {3:"류제협" , 100:"황민우"}

# 방법1
print(cabinet[3])
print(cabinet[100])

# 방법2
print(cabinet.get(3))
print(cabinet.get(100))

# 방법3
print(cabinet.get(3, "비었있음")) # 해당 번호의 값이 cabinet 안에 있으면 "~"문자 표기 안함
print(cabinet.get(5, "비었있음")) # 해당 번호의 값이 cabinet 안에 없으면 "~"문자 표기 

# 주의(차이점)
# print(cabinet[5])일 경우 오류시 프로그램 종료
# print(cabinet.get(5))일 경우 그냥 none으로 표기후 다음 코드 동작


cabinet = { "A-1" : "류제협", "B-32" : "황민우" }
print(cabinet["A-1"])
print(cabinet["B-32"])

print(cabinet)

# 값 추가 
cabinet["C-20"] = "이승우"
print(cabinet)
 
# 값 교체
cabinet["A-1"] = "성낙훈"
print(cabinet)

# 값 삭제
del cabinet["A-1"]
print(cabinet)

# key 값 출력
print(cabinet.keys())

# value 값 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 사전 비우기
cabinet.clear()
print(cabinet)



# 튜플 (리스트랑 다르게 내용 변경과 추가가 안됨 그러나 리스트에 비해 빠름)
menu = ("쫄면", "라면")
print(menu[0])
print(menu[1])

# 활용1
name = "류제협"
age = 26
hobby = "축구"
print(name, age, hobby)

# 활용2
(name, age, hobby) = ("류제협", 26, "축구")
print(name, age, hobby)