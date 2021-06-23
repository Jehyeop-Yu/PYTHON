# #자료구조 변경
# # 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu)) # 결과 : {'주스', '커피', '우유'} <class 'set'>

# menu = list(menu)
# print(menu, type(menu)) # 결과 : ['주스', '커피', '우유'] <class 'list'>

# menu = tuple(menu)
# print(menu, type(menu)) # 결과 : ('우유', '주스', '커피') <class 'tuple'>

# menu = set(menu)
# print(menu, type(menu)) # 결과 : {'커피', '주스', '우유'} <class 'set'>


# Quiz)
# 조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 smple을 활용


# from random import*
# lst = range(1, 21) # 1~20 까지 숫자 생성
# lst = list(lst) # 자료구조 변환 range -> list
# print(lst)
# shuffle(lst)

# a = randint(1,21)
# print(a)

# b = sample(lst,3)
# print(b)

# c = "-- 당첨자 발표 --\n치킨 당첨자 : " + str(a) + "\n커피 당첨자 : " + str(b) + "\n-- 축하합니다 --" 
# print(c)

from random import*
user = range(1, 21) # 1~20 까지 숫자 생성
user = list(user) # 자료구조 변환 range -> list
shuffle(user)
winners = sample(user, 4)

print("-- 당첨자 발표 --" )
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")