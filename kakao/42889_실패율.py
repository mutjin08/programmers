def solution(n, stages):
    nows = [0]*(n+2)
    for s in stages:
        nows[s] += 1
        
    dp = [0]*(n+2)
    dp[n+1] = nows[n+1]
    rates = {}
    for s in range(n, 0, -1):
        dp[s] = dp[s+1]+nows[s]
        
        r = 0 if dp[s]==0 else nows[s]/dp[s]
        if r not in rates:
            rates[r] = []
        rates[r].append(s)
    
    answer = []
    for r in sorted(rates, reverse=True):
        answer.extend(sorted(rates[r]))
    return answer