def solution(money):
    n = len(money)
    
    # 첫 집 털기 & 마지막 집 털지 않기
    firstDp = [0]*n
    firstDp[0], firstDp[1] = money[0], max(money[0], money[1])
    for i in range(2, n-1):
        firstDp[i] = max(firstDp[i-2]+money[i], firstDp[i-1])
    
    # 첫 집 털지 않기 & 마지막 집 털기
    lastDp = [0]*n
    lastDp[0], lastDp[1] = 0, money[1]
    for i in range(2, n):
        lastDp[i] = max(lastDp[i-2]+money[i], lastDp[i-1])

    return max(firstDp+lastDp)