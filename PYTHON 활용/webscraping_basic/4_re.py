# 정규식 
import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe

p = re.compile("ca.e") # p = 패턴
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, desination (o) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (o) | face (x)


def print_match(m):    
    if m:
        print("m.group():", m.group()) # 일치하는 문자열을 반환
        print("m.string:", m.string) # 입력받은 문자열 
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

# print(m.group()) # 매치되지 않으면 에러가 발생 


# m = p.match("case") # 주어진 문자열의 첨음부터 일치하는지 확인(앞에서부터 확인) -> carelese 입력시 care 를 출력
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는 부분이 있는지 확인
# print_match(m)

# lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환 -> ['care', 'cafe]
# print(lst) 

### < 정리 > ###

# 정규식 작성법 
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식 
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, desination (o) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (o) | face (x)

# 정규식 공부하는 사이트 
# w3schools.com -> python -> 좌측 목록 -> python RegEX