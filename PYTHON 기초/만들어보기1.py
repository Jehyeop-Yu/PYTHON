fruit = ["사과", "사과", "바나나","바나나", "딸기", "키위", "복숭아" ,"복숭아", "복숭아"]
x = len(fruit)
print(x)

d = {}

for f in fruit:
   if f in d:
       d[f] = d[f] + 1 
   else:
       d[f] = 1
print(d)
