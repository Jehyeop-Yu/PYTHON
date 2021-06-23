print(13 % 5) #나머지값만 표시
print(4 ** 2) #제곱
#문자열
x = "hello"
y = 'bye'
z = """
안녕하세요
등등 긴문자
"""

print(z)
print("안녕" + "하세요")
print("오늘 몇일이니? " + str(17) + "일 입니다.")

x = 4
y = "4"

print(str(x) + y) # -> "4" + "4" = "44" 문자 + 문자
print(x + int(y)) # -> 4 + ("4" -> 4) -> 4 + 4 = 8 // 숫자 + (문자->숫자) = 연산값

#불리언
x = True
y = False
print(x)
print(y)

#조건문
if 1 > 2:
    print("hello")
if 1 > 0 and 5 > 2: #and or == elif(= else if)
    print("hello2")
else:
    print("hi")

def chat(name1, name2, age):
    print("%s:너 몇 살이야?" % name1)
    print("%s:나? %d살이야" % (name2, age))

chat("윤하", "알렉스", 24) 
chat("철수", "영희", 16)

def sayHello(name, age):
    if age < 10:
        print("안녕," + name)
    elif age <= 20 and age >= 10:
        print("안녕하세요," + name)
    else:
        print("안녕하십니까, " + name + "님")

sayHello("제협", 5)
sayHello("워니", 10)
sayHello("알렉스", 20)
sayHello("윤하", 40)

for i in range(10): #range(N) 반복횟수
    print("dddd")

while i < 10:
    print("dddd")
    i = i + 1

#while True : ->무한루프
#break, continue
i = 0
while True:
    print("ddd")
    i = i + 1
    if i>2:
        break

#continue : continue다음의 동작은 안하고 다시처음 동작으로 돌려버린다.