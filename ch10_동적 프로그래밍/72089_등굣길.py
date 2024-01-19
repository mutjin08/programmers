from collections import deque

def bfs(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    
    for r in range(1, n+1):
        for c in range(1, m+1):
            if r==1 and c==1:
                continue
            if [c, r] in puddles:
                dp[r][c] = 0
                continue
            
            dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % 1000000007

    return dp[n][m]

def solution(m, n, puddles):
    return bfs(m, n, puddles)