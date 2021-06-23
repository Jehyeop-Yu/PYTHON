#리스트
subway = [10, 20, 30]
print(subway)

# 리스트화
subway = ["황민우", "류제협", "이승우", "성낙훈"] 
print(subway)

# 이승우가 몇번째위치에 있나?
print(subway.index("이승우"))

# 리스트에 추가
subway.append("김동현") # ['황민우', '류제협', '이승우', '성낙훈', '김동현']
print(subway)

# 리스트 사이에 추가
subway.insert(1, "김영권") # ['황민우', '김영권', '류제협', '이승우', '성낙훈', '김동현']
print(subway)

# 리스트 삭제 (뒤부터)
subway.pop()
print(subway) # ['황민우', '김영권', '류제협', '이승우', '성낙훈']

# 중복되는 리스트 확인
subway.append("류제협")
print(subway)
print(subway.count("류제협")) # count()안의 값이 몇번 나오나 확인

# 정렬 
num_list = [5, 2, 3, 4, 1]
num_list.sort()
print(num_list)

# 순서뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기 
num_list.clear()
print(num_list)

# 다양한 값으로 리스트 작성
mix_list = ["류제협", 20, True]
print(mix_list)

# 리스트 합치기
num_list.extend(mix_list) # num_list + mix_list
print(num_list)