#리플
x = ["nice to meet you"]
y = ["hello", 1,2,3,4]
z = [5,4,3,2,1]
z[2] = 7
print(x)
print(y)
print(x + y)
print(z[2])

num_elements = len(z)
print(num_elements)

a = sorted(z) #크기순으로 정리
print(a)

b = sum(z)
print(b)

for n in z: # n안에 차례대로 값을 넣어준다
    print(n)

print(z.index(2)) # index(N) N값이 몇번째 있는지 찾아준다
print(3 in z) # z안에 3이 있는지 true, false로 알려준다

#응용
if 4 in z:
    print("4가 존재해요!")
else:
    print("4가 존재하지 않아요!")


#튜플
t = (1,2,3)
w = ('a','b','c')
p = (1, "a", 2, "b")

# 동작은 튜플과 같지만 다음 안에 값을 바꿔주진 못한다.
# t[2] = 10 # 이 동작은 튜플에서 할수 없으므로 오류가 난다.
print(t)

#딕셔너리
q = {
    "name": "제협",
    "age": 26,
}
print(q["name"])
print(q["age"])
print(q.keys())
print(q.values())

for key in q:
    print("key: " + str(key))
    print("value: " + str(q[key]))

q["name"] = "류젭"
q["추가"] = "내용"
print(q)