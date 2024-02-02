#다시풀기
from collections import deque
def bfs(n, computers, visited, v):    
    q = deque([v])
    visited[v] = 1
    
    while q:
        v = q.popleft()
        for i in range(n):
            if computers[v][i]==1 and not visited[i]:
                q.append(i)
                visited[i] = 1
    
    return
    
def solution(n, computers):
    answer = 0
    visited = [0]*n
    for c in range(n):
        if not visited[c]:
            bfs(n, computers, visited, c)
            answer += 1
    return answer