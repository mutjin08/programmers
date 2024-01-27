# 단순 회전 구현
def spin_board(query, board):
    x1, y1, x2, y2 = [q-1 for q in query]
    
    temp = target = board[x1][y1]
    for i in range(x1, x2):
        board[i][y1] = board[i+1][y1]
        target = min(target, board[i][y1])
    for j in range(y1, y2):
        board[x2][j] = board[x2][j+1]
        target = min(target, board[x2][j])
    for i in range(x2, x1, -1):
        board[i][y2] = board[i-1][y2]
        target = min(target, board[i][y2])
    for j in range(y2, y1, -1):
        board[x1][j] = board[x1][j-1]
        target = min(target, board[x1][j])
    board[x1][y1+1] = temp
    
    return target

    

def solution(rows, columns, queries):
    answer = []
    board = [[i*rows+j+1 for j in range(columns)] for i in range(rows)]
    for query in queries:
        answer.append(spin_board(query, board))
    return answer
    

def solution(rows, columns, queries):
    board = [[i*rows+j+1 for j in range(columns)] for i in range(rows)]
    for query in queries:
        x = spin_board(query, board)
        print(x)
    return board