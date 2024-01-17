# failure
from itertools import permutations
def solution(numbers):
    answer = 0
    for number in permutations(map(str, numbers), len(numbers)):
        answer = max(answer, int("".join(number)))
    return str(answer)