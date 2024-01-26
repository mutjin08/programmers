from collections import deque

def bfs(v, graph, visited):
    q = deque([v])
    visited[v] = 1
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v]+1
    return visited.count(max(visited))

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    return bfs(1, graph, visited)