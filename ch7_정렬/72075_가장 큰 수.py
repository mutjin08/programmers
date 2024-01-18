def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse = True)
    
    #"0000"제거하기
    return str(int("".join(numbers)))