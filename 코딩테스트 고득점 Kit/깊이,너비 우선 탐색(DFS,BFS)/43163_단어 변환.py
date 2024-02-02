from collections import deque

def count_diff(word1, word2):
    cnt = 0
    for a, b in zip(word1, word2):
        if a!=b:
            cnt+=1
    if cnt==1:
        return True
    return False

def solution(begin, target, words):
    
    q = deque([[begin, 0]])
    visited = {}
    visited[begin] = 1
    
    while q:
        x, cnt = q.popleft()
        for w in words:
            if count_diff(x, w) and w not in visited:
                if w==target:
                    return cnt+1
                q.append([w, cnt+1])
                visited[w] = 1
    return 0