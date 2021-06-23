# # 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# open_account()

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money 

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1}원 입니다. ".format(commission, balance))

# # 함수 기본값 설정
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

# profile("유재석", 20,"파이썬")
# profile("김태호", 25,"자바")

# # 같은 학교 같은 학년 같은 반 같은 수업
# def profile(name, age=17,  main_lang="파이썬"): # 여기서 값을 지정해주면 그 값을 따르고 그게 아니면 아래에서 말해주는 값을 따른다
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# # 키워드로 함수 호출
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=20, name="김태호",)

# # 가변인자를 이용한 함수 호출 
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") # end = " " 는 print가 끝나고 비워준다 
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "python", "java", "c", "c++", "c#")
# profile("김태호", 25, "Kotlin", "swift", "", "", "")

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") # end = " " 는 print가 끝나고 비워준다 
#     for lang in language:
#         print(lang, end= " ")
#     print()

# profile("유재석", 20, "python", "java", "c", "c++", "c#")
# profile("김태호", 25, "Kotlin", "swift")

# # 지역변수(함수 내에서만 동작) & 전역변수(프로그램 어디서든 동작가능)
# gun = 10
# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     # gun = 20 # 지역변수
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
# print("[함수 외] 남은 총 : {0}".format(gun))

# # 활용
# gun = 10
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("[함수 외] 남은 총 : {0}".format(gun))

# # Quiz) 표준 체중을 구하는 프로그램을 작성하시오.

# # * 표준 체중 : 각 개인의 키에 적당한 체중

# # (성별에 따른 공식)
# #  남자 : 키(m) x 키(m) x 22
# #  여자 : 키(m) x 키(m) x 21

# # 조건1 : 표준 체중은 별도의 함수 내에서 계산
# #         * 함수명 : std_weight
# #         * 전달값 : 키(height), 성별(gender)
# # 조건2 : 표준 체중은 소수점 둘째자리까지 표시 

# # (출력 예제)
# # 키 175cm 남자의 표준 체중은 67.38kg 입니다. 

# 내가 만든거
def std_weight():
    index = 1
    while index >= 1:    
        gender = input("성별을 적으세요 (예시 : 남자, 여자) : ")
        if gender == "남자":
            height = input("키를 적으세요 : ")
            weight = (int(height)**2)*22/10000
            print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, round(weight,2)))
            print()
        elif gender == "여자":
            height = input("키를 적으세요 : ")
            weight = (int(height)**2)*21/10000
            print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, round(weight,2)))
            print()
        elif gender == "종료":
            index -= 1
            break            
std_weight()

# # 나도코딩
# def std_weight(height, gender): # 키는 m 단위(실수), 성별 "남자" / "여자"
#     if gender == "남자":
#         return height * height *22
#     else:
#         return height * height *21
# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight)) 