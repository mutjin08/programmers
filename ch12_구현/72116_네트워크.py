from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for v in range(n):
        if not visited[v]:
            q = deque([v])
            visited[v] = 1

            while q:
                v = q.popleft()
                for i in range(n):
                    if not visited[i]:
                        q.apphttps://school.programmers.co.kr/tryouts/72116/challenges?language=python3#end(i)
                        visited[i]=1       
            answer += 1
    return answer