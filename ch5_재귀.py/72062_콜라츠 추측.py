global cnt
cnt = 0

def solution(num):
    global cnt
    if cnt>=500:
        return -1
    elif num==1:
        return cnt
    elif num%2==0:
        cnt += 1
        return solution(num//2)
    elif num%2!=0:
        cnt += 1
        return solution(num*3+1)