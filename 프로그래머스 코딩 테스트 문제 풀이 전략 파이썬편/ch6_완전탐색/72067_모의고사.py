def solution(answers):
    scores = [0, 0, 0]
    sheets =[[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for idx in range(len(answers)):
        #1번 수포자
        i = idx%len(sheets[0]) if idx>=len(sheets[0]) else idx
        if sheets[0][i]==answers[idx]:
            scores[0]+=1
        #2번 수포자
        i = idx%len(sheets[1]) if idx>=len(sheets[1]) else idx
        if sheets[1][i]==answers[idx]:
            scores[1]+=1
        #3번 수포자
        i = idx%len(sheets[2]) if idx>=len(sheets[2]) else idx
        if sheets[2][i]==answers[idx]:
            scores[2]+=1
    
    answer=[]
    max_score = max(scores)
    for i in range(len(scores)):
        if scores[i]==max_score:
            answer.append(i+1)
    return answer