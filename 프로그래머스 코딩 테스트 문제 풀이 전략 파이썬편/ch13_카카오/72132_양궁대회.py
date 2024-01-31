from itertools import combinations_with_replacement

def compare(apeach, lion):
    aScore, lScore = 0, 0
    for i in range(11):
        if apeach[i] == lion[i]:
            continue
        elif apeach[i] >= lion[i]:
            aScore += i
        elif apeach[i] < lion[i]:
            lScore += i
    return lScore - aScore

def solution(n, apeach):
    apeach.reverse()
    answer = [-1]
    maxVal = 0
    for case in combinations_with_replacement(range(11), n):
        lion = [0 for _ in range(11)]
        for i in case:
            lion[i]+=1
        
        val = compare(apeach, lion)
        if val >= maxVal:
            answer = lion
    return answer