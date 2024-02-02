def solution(m, n, puddles):
    board = [[0 for _ in range(m+1)] for _ in range(n+1)]
    board[1][1] = 1
    for x in range(1, n+1):
        for y in range(1, m+1):
            if x==y==1:
                continue
            if [y, x] in puddles:
                board[x][y] = 0
                continue
            board[x][y] = (board[x-1][y] + board[x][y-1]) %1000000007
    return board[n][m]