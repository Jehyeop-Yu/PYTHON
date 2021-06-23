# # 파일 입출력
# # 파일 만들기(txt)
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# # 입력되어있는 txt파일에 덮어쓰기
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# # txt 파일 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# # 파일 줄별로 읽어오기 방법1
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# # 파일 줄별로 읽어오기 방법2
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end = "")
# score_file.close()

# # 파일 줄별로 읽어오기 방법3
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines :
#     print(line, end="")
# score_file.close()