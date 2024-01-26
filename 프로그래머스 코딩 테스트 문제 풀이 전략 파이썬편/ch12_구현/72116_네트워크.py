from collections import deque

def bfs(n, computers, visited, v):
    q = deque([v])
    visited[v] = 1
    
    while q:
        v = q.popleft()
        for i in range(n):
            #주의
            if not visited[i] and computers[v][i]==1:
                q.append(i)
                visited[i] = 1

def solution(n, computers):
    answer = 0
    visited = [0]*n
    
    for v in range(n):
        if not visited[v]:
            bfs(n, computers, visited, v)
            answer += 1
    return answer