def dec_to_n(target, n):
    result = ""
    while target:
        result = str(target%n) + result
        target //= n
    return list(result)

def solution(numbers):
    answer = []
    for number in numbers:
        x = dec_to_n(number, 2)
        
        if number%2==0:
            answer.append(number+1)
            
        elif number%2==1:
            x = ['0']+x
            p = len(x)-1
            while p>=0:
                if x[p]=='0':
                    break
                p -=1
            x[p] = '1'
            x[p+1] = '0'
        
            answer.append(int("".join(x), 2))
            
    return answer
            