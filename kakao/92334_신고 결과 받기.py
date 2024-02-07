def solution(id_list, report, k):
    dic = {}
    i = 0
    for user_id in id_list:
        dic[user_id] = i
        i += 1
    
    n = len(id_list)
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for r in report:
        f, t = r.split()
        f, t = dic[f], dic[t]
        graph[f][t] = 1
        
    banned = [sum(i) for i in zip(*graph)]
    for t in range(n):
        if banned[t] < k:
            for f in range(n):
                graph[f][t] = 0
    
    answer = [sum(i) for i in graph]
    return answer