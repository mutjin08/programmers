def solution(triangle):
    dp = [[0 for _ in range(i+1)] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for h in range(1, len(triangle)):
        dp[h][0] = dp[h-1][0] + triangle[h][0]
        for i in range(1, h):
            dp[h][i] = max(dp[h][i], dp[h-1][i-1]+triangle[h][i], dp[h-1][i]+triangle[h][i])
        dp[h][h] = dp[h-1][-1] + triangle[h][h]
    return max(dp[-1])