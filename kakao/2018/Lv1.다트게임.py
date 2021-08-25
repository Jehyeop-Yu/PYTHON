# 다트 게임은 총 3번의 기회로 구성된다.
# 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 0~10의 정수와 문자 S, D, T, *, '#'로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

# 조건1. 기회 3번
# 조건2. 기회당 얻을 수 잇는 점수 0~10점
# 조건3. 점수와 같이 Single(S)(1제곱), Double(D)(2제곱), Triple(T)(3제곱) 영역 존재 점수마다 존재
# 조건4. 스타상(*): 이전값과 현재값 2배 BUT,처음엔 첫번째 만 적용 , 스타상 중복 가능 중첩된 스타상 점수 4배 
# 조건5. 아차상('#') : 당첨시 해당 점수 마이너스 , 스타상과 중첩시 -2배  

# < 내가 푼거 >------------------------------------------------------
def solution(dartResult):
    answer = 0
    first = 0
    second = 0
    third = 0

    j = 0
    a = '0','1','2','3','4','5','6','7','8','9'
    b = 'S','D','T'
    c = '*','#'

    drlist = list(dartResult)
    for i in range(0,len(drlist)):

        if j == 0:
            if drlist[i] in a:
                if drlist[i-1] == '1' and drlist[i] =='0':
                    first = first + 9
                else:
                    first = first + int(drlist[i])
                    
            elif drlist[i] in b:
                if drlist[i] == 'S':
                    first = first**1
                elif drlist[i] == 'D':
                    first = first**2
                elif drlist[i] == 'T':
                    first = first**3
            
            elif drlist[i] in c:
                if drlist[i] == '*':
                    first = first*2
                elif drlist[i] == '#':
                    first = first*(-1)

        elif j == 1:    
            if drlist[i] in a:
                if drlist[i-1] == '1' and drlist[i] =='0':
                    second = second + 9
                else:
                    second = second + int(drlist[i])

            elif drlist[i] in b:
                if drlist[i] == 'S':
                    second = second**1
                elif drlist[i] == 'D':
                    second = second**2
                elif drlist[i] == 'T':
                    second = second**3
            
            elif drlist[i] in c:
                if drlist[i] == '*':
                    first = first*2
                    second = second*2
                elif drlist[i] == '#':
                    second = second*(-1)

        elif j == 2:    
            if drlist[i] in a:
                if drlist[i-1] == '1' and drlist[i] =='0':
                    third = third + 9
                else:
                    third = third + int(drlist[i])

            elif drlist[i] in b:
                if drlist[i] == 'S':
                    third = third**1
                elif drlist[i] == 'D':
                    third = third**2
                elif drlist[i] == 'T':
                    third = third**3

            elif drlist[i] in c:
                if drlist[i] == '*':
                    second = second*2 
                    third = third*2
                elif drlist[i] == '#':
                    third = third*(-1)

        if j < 2:
            if drlist[i] in b and drlist[i+1] in a:
                j = j+1
            elif drlist[i] in c and drlist[i+1] in a:
                j = j+1
            else:
                pass
    answer = first + second + third
    return answer

solution('1D2S3T*') 
# ------------------------------------------------------

# < 모범답안 >------------------------------------------------------
# 정규식 이용  힌트 "점수|보너스|[옵션]"
import re # 정규식 모듈 

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}

    option = {'' : 1, '*' : 2, '#' : -1}

    p = re.compile('(\d+)([SDT])([*#]?)')  # re.compile:정규식 사용, (\d): 0~9까지의 정수, [SDT] : SDT가 포함되어있는지 여부 , ? : 있어도 되고 없어도 되고

    dart = p.findall(dartResult) # findall 위 정규식과 매치해서 리스트로 돌려준다  ex) ['(\d+)([SDT])([*#]?)'+'(\d+)([SDT])([*#]?)'+'(\d+)([SDT])([*#]?)']
    print("dart=",dart)
    for i in range(len(dart)):

        print("dart[{}]=".format(i),dart[i])

        if dart[i][2] == '*' and i > 0: # option = '*' 일 경우 dart[i-1]에 *2 를 해라
            dart[i-1] *= 2

        print("dart[[{}][1]]=".format(i),dart[i][1])
        print("bonus[dart[{}][1]]=".format(i),bonus[dart[i][1]])
        
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
        
        print("dart =",dart)

    answer = sum(dart)
    print(answer)
solution('2T* 2D* 3D#')

# 1  '1S2D*3T'	37	11 * 2 + 22 * 2 + 33
# 2	'1D2S#10S'	9	12 + 21 * (-1) + 101
# 3	'1D2S0T'	3	12 + 21 + 03  --------------
# 4	'1S*2T*3S'	23	11 * 2 * 2 + 23 * 2 + 31
# 5	'1D#2S*3S'	5	12 * (-1) * 2 + 21 * 2 + 31
# 6	'1T2D3D#'	-4	13 + 22 + 32 * (-1)
# 7	'1D2S3T*'	59	12 + 21 * 2 + 33 * 2