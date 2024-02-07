from itertools import combinations

def solution(friends, gifts):
    n = len(friends)
    
    dic = {}
    i = 0
    for friend in friends:
        dic[friend] = i
        i+=1
    
    graph = [[0 for _ in range(n)] for _ in range(n)]
    scores = [0 for _ in range(n)]
    for gift in gifts:
        f, t = gift.split()
        f, t = dic[f], dic[t]
        graph[f][t] += 1
        scores[f] += 1
        scores[t] -= 1
    
    answer = [0 for _ in range(n)]
    for a, b in combinations(range(n), 2):
        if graph[a][b] > graph[b][a]:
            answer[a] += 1
        elif graph[b][a] > graph[a][b]:
            answer[b] += 1
        else:
            if scores[a] > scores[b]:
                answer[a] += 1
            elif scores[a] < scores[b]:
                answer[b] += 1
            else:
                continue
    return max(answer)