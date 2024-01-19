def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, total+1):
        j = total/i
        if j%1!=0:
            continue
        j = int(j)
        
        if (i-2)*(j-2)==yellow:
            return [j,i]
    return -1