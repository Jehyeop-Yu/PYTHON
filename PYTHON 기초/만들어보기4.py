# 문자열
print("나는 %d살 입니다." % 26) # %d = 정수
print("나는 %s을 좋아해요" % "파이썬") # %S = 문자열
print("APPLE 은 %c로 시작해요." % "A") # %C =  문자

print("나는 %s살 입니다" %26)
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨강")) # 여러개 넣기 방법 1
print("나는 {}살 입니다.".format(26))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨강")) # 여러개 넣기 방법 2
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨강")) # 여러개 넣기 방법 3-1
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨강")) # 여러개 넣기 방법 3-2

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 26, color = "흰")) 
print("나는 {color}살이며, {age}색을 좋아해요.".format(age = 26, color = "흰"))

# # 탈출문자
# \n = 줄바꿈
print("백문이 불여일견 \n백견이 불여일타") # \n = 줄바꿈

print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\" 입니다.")
print("저는 \'나도코딩\' 입니다.")

# \\ : 문장 내에서 \

# \r : 커서를 맨앞으로이동
print("Red Apple\rPine")

#\b : 백스페이스(한글자 삭제)
print("Redd\bApple")

#\t : 탭
print("Red\tApple")

url = "http://Youtube.com"
my_str = url.replace("http://", "") # 다시 설정해주기, 해당하는부분 제외
print(my_str) # naver.com
my_str = my_str[:my_str.index(".")] # .이전까지의 값만 표기
print(my_str) # naver
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)
print("{0}의 비밀번호는 {1}입니다".format(url, password))