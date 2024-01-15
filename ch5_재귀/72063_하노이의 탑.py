def hanoi(n, start, mid, end):
    if n==1:
        return [[start, end]]
    
    answer = []
    answer += hanoi(n-1, start, end, mid)
    answer += [[start, end]]
    answer += hanoi(n-1, mid, start, end)
    
    return answer
    
    
def solution(n):
    answer = hanoi(n, 1, 2, 3)
    return answer