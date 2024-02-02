def solution(numbers, target):
    results = [-numbers[0], numbers[0]]
    for number in numbers[1:]:
        temp = []
        for result in results:
            temp.append(result + number)
            temp.append(result - number)
        results = temp
    return results.count(target)