# 왜 board를 뒤집어서 내야 하는거지?
from itertools import combinations

def draw_star(spots):
    minX, minY = [min(i) for i in zip(*spots)]
    maxX, maxY = [max(i) for i in zip(*spots)]
    
    sizeX = maxX - minX + 1
    sizeY = maxY - minY + 1

    board = [["." for _ in range(sizeX)] for _ in range(sizeY)]
    for x, y in spots:
        board[y-minY][x-minX] = "*"
    
    board = ["".join(i) for i in board][::-1]
    return board
        

def find_cross(l1, l2):
    a, b, e = l1
    c, d, f = l2
    
    if a*d-b*c==0:
        return [False, -1, -1]
    
    x = (b*f-e*d)/(a*d-b*c)
    y = (e*c-a*f)/(a*d-b*c)
    
    if x%1==0 and y%1==0:
        return [True, int(x), int(y)]
    
    return [False, -1, -1]

def solution(line):
    spots = []
    for l1, l2 in combinations(line, 2):
        result = find_cross(l1, l2)
        if result[0]:
            spots.append((result[1], result[2]))
    spots = list(set(spots))
    return draw_star(spots)
        