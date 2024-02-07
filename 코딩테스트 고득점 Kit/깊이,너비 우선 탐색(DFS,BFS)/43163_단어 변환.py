from collections import deque

def one_diff(a, b):
    answer = 0
    for i in range(len(a)):
        if a[i]!=b[i]:
            answer += 1
    if answer==1:
        return True
    return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    while q:
        print(q)
        x, cnt = q.popleft()
        if x == target:
            return cnt
        
        for word in words:
            if one_diff(x, word):
                q.append((word, cnt+1))
    return 0
    