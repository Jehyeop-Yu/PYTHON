
jumin = "990120-1234567"
print ("성별 : " + jumin[7])
print ("연 : " + jumin[0:2]) # 0 부터 2 직전까지
print ("월 : " + jumin[2:4])
print ("일 : " + jumin[4:6])
print ("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print ("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
print ("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7 번째부터 끝까지

python = "Python is Amazing"
print(python.lower()) # 소문자로 표기
print(python.upper()) # 대무자로 표기
print(python[0].isupper()) # n번째 글자가 대문자인가?
print(len(python))
print(python.replace("Python", "Java")) # 문자를 선택해서 바꿔주기

index = python.index("n") # n 의 위치 찾기 
print(index)
index = python.index("n", index + 1) # 첫번째 n 이후 n 의 위치 찾기
print(index)

print(python.find("Java")) # 원하는 값이 없으면 -1출력 (출력은 가능)
# print(python.index("Java")) # 원하는 값이 없으면 오류 (출력불가)

print(python.count("n")) # n 의 갯수 count