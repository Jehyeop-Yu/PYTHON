import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
        
def solution(n,t,m,p):
    kk = ''
    for x in range(0,100):
        kk = kk + convert(x,n).upper()
    x = list(kk)[p-1:t*m+p-1:m]
    answer="".join(map(str, x))
    # return answer
    print('출력값 =',answer) # 2진수 
solution(14,16,2,2)


# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다
# n	   t	m	p	result
# 2	   4	2	1	"0111"
# 16   16	2	1	"02468ACE11111111"
# 16   16	2	2	"13579BDF01234567"