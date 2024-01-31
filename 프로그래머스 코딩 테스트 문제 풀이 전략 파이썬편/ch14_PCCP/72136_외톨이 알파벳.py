def solution(target):
    dic = {}
    answer = []
    
    dic[target[0]] = 1
    for i in range(1, len(target)):
        if target[i]!=target[i-1]:
            if target[i] in dic:
                answer.append(target[i])
            elif target[i] not in dic:
                dic[target[i]] = 1
    answer = "".join(sorted(list(set(answer))))
    if len(answer)==0:
        return "N"
    return answer