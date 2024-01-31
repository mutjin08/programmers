def solution(nodeinfo):
    graph = {}
    for x, y in nodeinfo:
        if y not in graph:
            graph[y] = []
        graph[y].append(x)
    return graph