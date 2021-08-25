# numbers = '순서대로 누를 번호가 담긴 배열' 1 <= numbers <=1000  <- 원소 0~9
# hand = '왼손잡이인지 오른손잡이인 지를 나타내는 문자열 ' "left" , "right" 
# '각 번호를 누른 엄지손가락이 ''왼손인 지 오른손인 지''를 나타내는 연속된 문자열 형태로 return'
# L = '왼손사용' 
# R = '오른손사용'
# "right" = R
# "left" = L
# <내가 푼거>-----------------------------------------------------------
def solution(numbers, hand):
    keypad = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
    Lpush = keypad['*']
    Rpush = keypad['#']
    answer = ''
    for i in numbers:
        push = keypad[i]
        if i in [1,4,7]:
            answer += 'L'
            Lpush = push
        elif i in [3,6,9]:
            answer += 'R'
            Rpush = push
        elif i in [2,5,8,0]:
            hand_L = 0
            hand_R = 0
            for a,b,c in zip(Lpush, Rpush, push):
                hand_L += abs(a-c)
                hand_R += abs(b-c)
            if hand_L < hand_R:
                answer += 'L'
                Lpush = push
            elif hand_L > hand_R:
                answer += 'R'
                Rpush = push
            else:
                if hand == 'left':
                    answer +='L'
                    Lpush = push
                else:
                    answer +='R'
                    Rpush = push
            
    return answer
    print(answer)

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right") # "LRLLLRLLRRL"
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left") # "LRLLRRLLLRR"

