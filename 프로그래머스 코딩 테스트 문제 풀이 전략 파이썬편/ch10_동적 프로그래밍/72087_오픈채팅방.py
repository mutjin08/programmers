# 다시풀기

def solution(n, target):
    if target==1:
        return 1
    
    dp = []
    for i in range(1, 9):
        temp = set()
        temp.add(int(str(n)*i))
        for j in range(i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    temp.add(op1 + op2)
                    temp.add(op1 - op2)
                    temp.add(op1 * op2)
                    if op2!=0:
                        temp.add(op1 // op2)
        if target in temp:
            return i
        dp.append(temp)
    return -1