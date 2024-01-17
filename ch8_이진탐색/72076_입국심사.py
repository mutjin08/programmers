def solution(n, times):
    answer = -1
    left, right = 1, max(times)*n
    
    while left<=right:
        mid = (left+right)//2
        
        passed = 0
        for time in times:
            passed += mid//time
            if passed>=n:
                break
        
        if passed >= n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    return answer
            