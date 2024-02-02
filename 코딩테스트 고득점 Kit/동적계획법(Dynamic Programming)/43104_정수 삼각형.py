def solution(triangle):
    triangle = [[0] + t + [0] for t in triangle]
    for h in range(1, len(triangle)):
        for i in range(1, h+2):
            triangle[h][i] += max(triangle[h-1][i-1], triangle[h-1][i])
    return max(triangle[-1])