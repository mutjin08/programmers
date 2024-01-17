def solution(rows, columns, queries):
    board = [[i*columns+j+1 for j in range(columns)] for i in range(rows)]
    for x1, y1, x2, y2 in queries:
        temp = board[x1][y2]
        for y in range(y1, y2):
            board[x1][y] = 
    return board