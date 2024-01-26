from itertools import permutations
def calc(nums, op):
    if op=="+":
        return sum(nums)
    elif op=="-":
        return nums[0]-sum(nums[1:])
    elif op=="*":
        answer = 1
        for num in nums:
            answer *= num
        return answer

def solution(expression):
    answer = -1
    for operator in permutations(['+', '-', '*'], 3):
        expressions = expression.split(operator[0])
        for i in range(len(expressions)):
            expressions[i] = expressions[i].split(operator[1])
            for j in range(len(expressions[i])):
                expressions[i][j] = list(map(int, expressions[i][j].split(operator[2])))
                expressions[i][j] = calc(expressions[i][j], operator[2])
            expressions[i] = calc(expressions[i], operator[1])
        expressions = calc(expressions, operator[0])
        answer = max(answer, abs(expressions))
        
    return answer