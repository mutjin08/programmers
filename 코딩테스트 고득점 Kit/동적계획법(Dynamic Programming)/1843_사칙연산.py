# 다시풀기
def solution(arr):
    nums = [int(a) for a in arr[::2]]
    ops = [a for a in arr[1::2]]
    n = len(nums)
    
    minDp = [[0 for _ in range(n)] for _ in range(n)]
    maxDp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        minDp[i][i] = nums[i]
        maxDp[i][i] = nums[i]
    
    for size in range(1, n):
        for start in range(0, n):
            end = start + size
            if end >= n:
                continue
            
            minCands = []
            maxCands = []
            
            for i in range(start+1, end+1):
                if ops[i-1] == "-":
                    maxCands.append(maxDp[start][i-1] - minDp[i][end])
                    minCands.append(minDp[start][i-1] - maxDp[i][end])
                elif ops[i-1] == "+":
                    maxCands.append(maxDp[start][i-1] + maxDp[i][end])
                    minCands.append(minDp[start][i-1] + minDp[i][end])
            maxDp[start][end] = max(maxCands)
            minDp[start][end] = min(minCands)
    return maxDp[0][n-1]