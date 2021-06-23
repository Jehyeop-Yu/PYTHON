# pickle (데이터를 파일 형태로 저장)
# import pickle

# # 파일 작성 및 저장
# profile_file = open("profile.pickle", "wb") # W : 쓰기목적
# profile = {"이름":"박명수", "나이": 30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close()

# # 작성된 파일 정보를 불러오기
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile 에 불러오기 
# print(profile)
# profile_file.close()

# # with
# with open("profile.pickle", "rb") as profile_file :  # "profile.pickle"파일을 열어서 "profile_file" 의 변수에 저장
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


# Quiz ) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출려되어야 합니다.

# - X 주차 주간 보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일 명은 '1주차.txt','2주차.txt',... 와 같이 만듭니다. 

# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n 부서 : ")
#         report_file.write("\n 이름 : ")
#         report_file.write("\n 업무 요약 : ")