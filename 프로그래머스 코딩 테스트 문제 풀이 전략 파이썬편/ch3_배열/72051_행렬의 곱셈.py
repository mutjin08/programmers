def solution(arr1, arr2):
    answer = []
    for i in arr1:
        temp = []
        for j in zip(*arr2):
            temp.append(sum(a*b for a, b in zip(i, j)))
        answer.append(temp)
    return answer