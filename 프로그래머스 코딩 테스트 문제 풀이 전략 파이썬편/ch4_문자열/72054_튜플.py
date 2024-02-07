def solution(s):
    tuples = []
    for a in s.split("},"):
        a = a.replace("{", "").replace("}", "").split(",")
        tuples.append(a)
    tuples.sort(key = len)
    
    answer = []
    for tup in tuples:
        for num in tup:
            num = int(num)
            if num not in answer:
                answer.append(num)
    return answer