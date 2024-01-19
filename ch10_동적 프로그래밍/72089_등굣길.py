# error
from collections import deque

def bfs(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][1] = 1
    for j in range(1, m+1):
        dp[1][j] = 1
    
    for r in range(2, n+1):
        for c in range(2, m+1):
            if [c, r-1] not in puddles:
                dp[r][c]+=dp[r-1][c]
            if [c-1, r] not in puddles:
                dp[r][c]+=dp[r][c-1]

    return dp[n][m]%1000000007

def solution(m, n, puddles):
    return bfs(m, n, puddles)