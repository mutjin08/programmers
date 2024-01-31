from heapq import heappush, heappop
def solution(ability, number):
    h = []
    for a in ability:
        heappush(h, a)
    
    for _ in range(number):
        x = heappop(h)
        y = heappop(h)
        heappush(h, x+y)
        heappush(h, x+y)
    return sum(h)