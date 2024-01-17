from itertools import combinations
def solution(line):
    spots = []
    for line1, line2 in combinations(line, 2):
        a, b, e = line1
        c, d, f = line2
        if a*d-b*c==0:
            continue
        x = (b*f-e*d)//(a*d-b*c)
        y = (e*c-a*f)//(a*d-b*c)
        if x%1!=0 or y%1!=0:
            continue
        spots.append((x, y))
    return list(set(spots))