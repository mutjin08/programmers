def attack(r1, c1, r2, c2, degree, board):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            board[i][j] -= degree
    return board

def heal(r1, c1, r2, c2, degree, board):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            board[i][j] += degree
    return board

def solution(board, skill):
    n, m = len(board), len(board[0])
    for t, r1, c1, r2, c2, degree in skill:
        if t==1:
            attack(r1, c1, r2, c2, degree, board)
        elif t==2:
            heal(r1, c1, r2, c2, degree, board)
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                answer+=1
    return answer