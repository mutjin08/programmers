def solution(s):
    tuples = []
    for a in s.split('},'):
        tuples.append(a.replace('{', '').replace('}', '').split(','))
    tuples.sort(key = len)
    
    answer = []
    for tup in tuples:
        for i in tup:
            i = int(i)
            if i not in answer:
                answer.append(i)
                break
    
    return answer