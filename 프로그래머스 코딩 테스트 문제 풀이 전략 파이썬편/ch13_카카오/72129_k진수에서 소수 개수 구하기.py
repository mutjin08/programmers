def is_prime(x):
    if x<2:
        return False
    
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    
    return True

def dec_to_k(n, k):
    answer = ""
    while n>0:
        answer = str(n%k) + answer
        n //= k
    return answer

def solution(n, k):
    answer = 0
    for x in dec_to_k(n, k).split("0"):
        if len(x)>0 and is_prime(int(x)):
            answer += 1
    return answer