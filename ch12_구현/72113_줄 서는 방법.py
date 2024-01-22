# 효율성 실패
from itertools import permutations
def solution(n, k):
    cnt = 1
    for case in permutations([i+1 for i in range(n)]):
        if cnt==k:
            return list(case)
        cnt += 1