# # if
# weather = input("오늘 날씨 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("아무 문제 없어요")

# temp = int(input("기온이 어때요? "))
# if 30 <= temp:
#     print("너무 더워요, 나가지 마세요")
# elif 10 <= temp and temp <30 :
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요 나가지 마세요")

# # for
# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(5):
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}님 커피가 준비되었습니다.".format(customer))

# # while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}님 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# person = "unknown"

# while person != customer :
#     print("{0}님 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# # continue
# absent = [2, 5] # 결석
# lost_book = [7] # 책이 없음
# for student in range(1, 11): # 번호
#     if student in absent:
#         continue # absent에 해당하면 건너뛴다.
#     elif student in lost_book:
#         print("오늘 수업은 여기까지, {0}번은 교무실로 따라봐".format(student))
#         break
#     print("{0}번 책읽어".format(student))

# # for문 활용
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생들 이름을 길이로 변환
# students = ["Iron man", "Thor", "Groot"]
# students = [len(i) for i in students] # students -> i -> len -> i
# print(students)

# # 학생들 이름을 대문자로 변환
# students = ["Iron man", "Thor", "Groot"]
# students = [i.upper() for i in students] # students -> i -> upper -> i
# print(students)

# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다. 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 만들어라

# 조건1 : 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해진다.
# 조건2 : 당신은 소요시간 5 ~ 15분 사이의 승객만 매칭해야한다. 

# (출력문 예제)
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [o] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

from random import *
cnt = 0
for guest in range(1, 51):
    time = randint(4,51)
    if time < 16 :
        ox = "O"
        cnt += 1
    else:
        ox = " "
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(ox, guest, time))
print("총 탑승 승객 : {0}분".format(cnt))