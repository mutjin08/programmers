def solution(n, results):
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for w, l in results:
        graph[w][l] = 1
        graph[l][w] = -1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i==j:
                    continue
                if graph[i][j]==1 or graph[i][j]==-1:
                    continue
                
                # i > k > j
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[k][i] = graph[j][k] = graph[j][i] = -1
                    
    answer = 0
    for player in graph:
        if player.count(0)==2:
            answer+=1
    return answer