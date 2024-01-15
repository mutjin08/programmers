def solution(num):
    cnt = 0
    while cnt<=500:
        if num==1:
            return cnt
        cnt += 1
        if num%2==0:
            num//=2
        elif num%2!=0:
            num*=3
            num+=1
    return -1