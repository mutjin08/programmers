global cnt
cnt = 0
def solution(num):
    global cnt
    
    if cnt>=500:
        return -1
    elif num==1:
        return cnt
    
    cnt += 1
    
    if num%2==0:
        return solution(num//2)
    elif num%2!=0:
        return solution(num*3+1)