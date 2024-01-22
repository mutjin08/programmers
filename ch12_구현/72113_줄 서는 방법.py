# 효율성 실패 -> 성공 but 다시풀기
from itertools import permutations

def factorial(n):
    if n==1:
        return 1
    dp = [1]*(n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1]*i
    return dp[n]

def solution(n, k):
    answer = []
    
    
    people = [i+1 for i in range(n)]
    while n>0:
        fact = factorial(n-1)
        answer.append(people.pop((k-1)//fact))
        k %= fact
        n -= 1
        
        
    return answer
        