from itertools import permutations

def is_prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(numbers):
    splits = []
    for i in range(1, len(numbers)+1):
        for n in permutations(numbers,i):
            splits.append(int("".join(n)))
    splits = list(set(splits))
    
    answer = 0
    for n in splits:
        if is_prime(n):
            answer+=1
            
    return answer