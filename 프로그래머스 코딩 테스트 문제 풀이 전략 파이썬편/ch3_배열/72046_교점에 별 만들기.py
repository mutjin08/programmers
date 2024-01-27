from itertools import combinations

def draw(spots):
    mins, maxs = [], []
    for target in zip(*spots):
        mins.append(min(target))
        maxs.append(max(target))
    
    x_size, y_size = maxs[0]-mins[0]+1, maxs[1]-mins[1]+1
    board = [["." for _ in range(x_size)] for _ in range(y_size)]
    return board

def solution(line):
    spots = []
    for line1, line2 in combinations(line, 2):
        a, b, e = line1
        c, d, f = line2
        if a*d-b*c==0:
            continue
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
        if x%1!=0 or y%1!=0:
            continue
        spots.append((int(x), int(y)))
    spots = list(set(spots))
    
    return draw(spots)from itertools import combinations

def draw(spots):
    mins, maxs = [], []
    for target in zip(*spots):
        mins.append(min(target))
        maxs.append(max(target))
    
    x_size, y_size = maxs[0]-mins[0]+1, maxs[1]-mins[1]+1
    board = [["." for _ in range(x_size)] for _ in range(y_size)]
    return board

def solution(line):
    spots = []
    for line1, line2 in combinations(line, 2):
        a, b, e = line1
        c, d, f = line2
        if a*d-b*c==0:
            continue
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
        if x%1!=0 or y%1!=0:
            continue
        spots.append((int(x), int(y)))
    spots = list(set(spots))
    
    return draw(spots)from itertools import combinations

def draw(spots):
    mins, maxs = [], []
    for target in zip(*spots):
        mins.append(min(target))
        maxs.append(max(target))
    
    x_size, y_size = maxs[0]-mins[0]+1, maxs[1]-mins[1]+1
    board = [["." for _ in range(x_size)] for _ in range(y_size)]
    return board

def solution(line):
    spots = []
    for line1, line2 in combinations(line, 2):
        a, b, e = line1
        c, d, f = line2
        if a*d-b*c==0:
            continue
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
        if x%1!=0 or y%1!=0:
            continue
        spots.append((int(x), int(y)))
    spots = list(set(spots))
    
    return draw(spots)from itertools import combinations

def draw(spots):
    mins, maxs = [], []
    for target in zip(*spots):
        mins.append(min(target))
        maxs.append(max(target))
    
    x_size, y_size = maxs[0]-mins[0]+1, maxs[1]-mins[1]+1
    board = [["." for _ in range(x_size)] for _ in range(y_size)]
    return board

def solution(line):
    spots = []
    for line1, line2 in combinations(line, 2):
        a, b, e = line1
        c, d, f = line2
        if a*d-b*c==0:
            continue
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
        if x%1!=0 or y%1!=0:
            continue
        spots.append((int(x), int(y)))
    spots = list(set(spots))
    
    return draw(spots)from itertools import combinations

def draw(spots):
    mins, maxs = [], []
    for target in zip(*spots):
        mins.append(min(target))
        maxs.append(max(target))
    
    x_size, y_size = maxs[0]-mins[0]+1, maxs[1]-mins[1]+1
    board = [["." for _ in range(x_size)] for _ in range(y_size)]
    return board

def solution(line):
    spots = []
    for line1, line2 in combinations(line, 2):
        a, b, e = line1
        c, d, f = line2
        if a*d-b*c==0:
            continue
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
        if x%1!=0 or y%1!=0:
            continue
        spots.append((int(x), int(y)))
    spots = list(set(spots))
    
    return draw(spots)