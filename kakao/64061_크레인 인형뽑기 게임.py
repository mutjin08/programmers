def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    for m in moves:
        m-=1
        picked = 0
        #index caution
        for h in range(n):
            if board[h][m]==0:
                continue
            stack.append(board[h][m])
            board[h][m] = 0
            picked = 1
            break
            
        if not picked or len(stack)<2:
            continue
        if stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
    return answer