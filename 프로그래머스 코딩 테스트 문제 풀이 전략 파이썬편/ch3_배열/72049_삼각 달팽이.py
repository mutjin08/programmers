def solution(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    x, y = -1, 0
    cnt = 1
    
    for i in range(n):
        for _ in range(n-i):
            if i%3==0:
                x+=1 #down
            elif i%3==1:
                y+=1 #right
            elif i%3==2:
                x-=1
                y-=1 #up

            board[x][y] = cnt
            cnt += 1
    
    answer = []
    for i in range(n):
        answer.extend(board[i][:i+1])
    return answer