# bfs
from collections import deque
def solution(numbers, target):
    q = deque([[numbers[0], 0], [-numbers[0], 0]])
    n = len(numbers)
    answer = 0
    
    while q:
        val, idx = q.popleft()
        idx += 1
        if idx<n:
            q.append([val+numbers[idx], idx])
            q.append([val-numbers[idx], idx])
        elif idx==n:
            if val==target:
                answer+=1
                
    return answer
            
        