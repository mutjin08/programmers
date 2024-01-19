def solution(triangle):
    answer = 0
    dp = [0]*len(triangle)
    dp[0] = triangle[0][0]
    for h in range(1, len(triangle)):
        dp[h] = dp[h-1]+triangle[h][0]
        for i in range(1, h+1):
            dp[h] = max(dp[h],dp[h-1]+triangle[h][i-1], dp[h-1]+triangle[h][i])
    return dp