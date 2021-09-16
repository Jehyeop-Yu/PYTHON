# 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)

# 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램

# 높이 m, 폭 n과 판의 배치 정보 board
# 2 ≦ n, m ≦ 30

# 문자는 대문자 A에서 Z가 사용된다.
# 4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"] 14
# "CCBDE",
# "AAADE",
# "AAABF",
# "CCBBF"

def solution(m, n, board):
    x = range(m)
    y = range(n)
    position = {}
    for board_x in x:
        for board_y in y:
            pos = board_x,board_y
            word = board[board_x][board_y]
            position[pos] = word
    def rec():
        for i in x:

    print(position[1,1])


solution(4,	5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])