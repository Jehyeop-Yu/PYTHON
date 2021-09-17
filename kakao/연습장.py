def solution(m, n, board):
    x = range(m)
    y = range(n)
    position = {}
    for board_x in x:
        for board_y in y:
            pos = board_x,board_y
            word = board[board_x][board_y]
            position[pos] = word
    
    for i in range(m-1):
        for j in range(n-1):
            if position[i,j] == position[i+1,j] == position[i,j+1] == position[i+1,j+1]:
                position[i,j] = '0'
                position[i+1,j] = '0'
                position[i,j+1] = '0'
                position[i+1,j+1] = '0'
            
    print(position)

solution(4,	5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])

c추가추가추가추가추가