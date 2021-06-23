# 집합 (set) -> 중복x, 순서x
my_set = {1,2,3,3,3}
print(my_set)

java = {"류제협", "황민우", "이승우", "성낙훈"}
python = set(["류제협", "김동현"])

# 교집합 (둘다 가능)
print(java & python)
print(java.intersection(python))

# 합집합 (둘 중 하나만 가능해도 선택)
print(java | python)
print(java.union(python))

# 차집합 (java 가능 하지만 python은 불가능)
print(java - python)
print(java.difference(python))

# 값 추가
python.add("김영권")
print(python)

# 값 제외
java.remove("성낙훈")
print(java)