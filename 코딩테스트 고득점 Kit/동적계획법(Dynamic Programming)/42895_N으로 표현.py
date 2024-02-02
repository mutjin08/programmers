def solution(a, target):
    dp = [{}]
    
    for n in range(1, 9):
        temp = set()
        temp.add(int(str(a)*n))
        
        for i in range(1, n):
            for op1 in dp[i]:
                for op2 in dp[n-i]:
                    temp.add(op1+op2)
                    temp.add(op1-op2)
                    temp.add(op1*op2)
                    if op2!=0:
                        temp.add(op1/op2)
                        
        if target in temp:
            return n
        dp.append(temp)
    return -1