# 표준 입출력
print("Python","Java")
print("Python","Java",sep=",")
print("Python","Java","JavaScript",sep=" vs ") # 문장 사이사이 문구를 입력해준다.

print("Python","Java",sep=",",end="?") # end 문장의 끝부분을 ~로 바꿔준다, 다음 문장이 연달아 출력
print(" 무엇이 더 재밌을까요?")

import sys
print("Python","Java", file=sys.stdout) # 표준 출력
print("Python","Java", file=sys.stderr) # 표준 에러 

# 정렬
scores = {"수학" : 80, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=" : ") # ljust(L) 정렬 기준 8칸 띄우기, rjust(R) 정렬 기준 4칸 띄우기 

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1,21):
    print("대기번호 : ", str(num).zfill(3)) # zfill(n) n자릿수만큼 표기 빈자리는 0으로 표시 

answer = input("아무값이나 입력하세요 : ") # input으로 받아오는 값은 문자열(str)로 된다.
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))  # >오른쪽 정렬, <왼쪽 정렬

# 양수 일때는 +로 표시, 음수 일때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸은 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 콤마를 찍어주기 
print("{0:,}".format(100000000000000))

# 3자리 마다 콤마를 찍어주기, +-부호 붙이기
print("{0:+,}".format(100000000000000))

# 3자리 마다 콤마 찍어주기, 부호도 붙이고, 자릿수 확보하기 
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채우기
print("{0:^<+30,}".format(100000000000000))

# {0:ABCDE}
# 정리 A = 빈칸에 표시할 기호 넣기, B = < (왼쪽 정렬) or > (오른쪽 정렬), C = +-부호넣기, D = 표기할 자릿수, E = , 3자릿수 마다 표기  

# 소수점 출력 
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시 ( 소수점 3째 자리에서 반올림 )
print("{0:.2f}".format(5/3))