def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left, right = 1, distance
    while left <= right:
        mid = (left+right)//2
        
        prev_rock = 0
        remove_cnt = 0
        for now_rock in rocks:
            dist = now_rock - prev_rock
            if dist < mid:
                remove_cnt += 1
                if remove_cnt > n:
                    break
            else:
                prev_rock = now_rock
                
        if remove_cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer

