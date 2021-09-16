
# < 내가 푼거 >------------------------------------------------------
def solution(msg):
    LZW = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14,
             'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    j = 2
    answer = []
    while j != 0 :
        if (msg[0:j-1] in LZW) and (msg[0:j] not in LZW):
            answer.append(LZW[msg[0:j-1]])
            LZW[msg[0:j]] = len(LZW)+1
            msg = msg[j-1:]
            j = 2
            if msg in LZW:
                answer.append(LZW[msg])
                break
        elif (msg[0:j-1] in LZW) and (msg[0:j] in LZW):
            j = j+1
            if msg in LZW:
                answer.append(LZW[msg])
                break
    return answer
    print(answer)
solution('TOBEORNOTTOBEORTOBEORNOT')
# solution('KAKAO') #[11, 1, 27, 15]
# -----------------------------------------------------------------

# < 모범답안 >------------------------------------------------------
def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer
# -----------------------------------------------------------------
