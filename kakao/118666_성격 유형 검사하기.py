def solution(survey, choices):
    dic = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    scores = [0, 3, 2, 1, 0, 1, 2, 3]
    
    for category, choice in zip(survey, choices):
        if choice<=4:
            dic[category[0]]+=scores[choice]
        else:
            dic[category[1]]+=scores[choice]
            
    characters = [["R","T"], ["C","F"], ["J","M"], ["A","N"]]
    answer = ""
    for a, b in characters:
        if dic[a] >= dic[b]:
            answer += a
        elif dic[b] > dic[a]:
            answer += b
    return answer