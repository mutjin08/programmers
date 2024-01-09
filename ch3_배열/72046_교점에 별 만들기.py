from itertools import combinations

def draw_stars(spots):
    answer = [[],[]]
    for ss in zip(*spots):
        answer[0].append(min(ss))
        answer[1].append(max(ss))
        
    size_x = answer[1][0] - answer[0][0] + 1
    size_y = answer[1][1] - answer[0][1] + 1
    
    board = [["." for _ in range(size_x)] for _ in range(size_y)]
    for x, y in spots:
        x -= answer[0][0]
        y -= answer[0][1]
        board[y][x] = "*"
    
    board = ["".join(b) for b in board]
    return board[::-1]

def solution(line):
    spots = []
    
    for l1, l2 in combinations(line, 2):
        a, b, e = l1
        c, d, f = l2
        
        if a*d-b*c==0:
            continue
        
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
        
        if x%1==0 and y%1==0:
            spots.append((int(x), int(y)))
            
    return draw_stars(spots)