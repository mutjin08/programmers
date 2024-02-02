from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    q = deque([(0, 0, 1)])
    visited[0][0] = 1
    
    while q:
        x, y, dist = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]:
                if nx==n-1 and ny==m-1:
                    return dist+1
                q.append((nx, ny, dist+1))
                visited[nx][ny] = 1
    return -1