def solution(cap, n, deliveries, pickups):
    answer = 0
    bag = [0, 0]
    
    for i in range(n-1, -1, -1):
        bag[0] += deliveries[i]
        bag[1] += pickups[i]
        
        while bag[0]>0 or bag[1]>0:
            bag[0] -= cap
            bag[1] -= cap
            answer += (i+1)*2 #주의
    return answer