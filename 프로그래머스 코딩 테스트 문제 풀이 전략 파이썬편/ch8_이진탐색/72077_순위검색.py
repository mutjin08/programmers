from copy import deepcopy
def parsed_info(infos):
    answer = {}
    for info in infos:
        info = info.split()
        score = int(info.pop())
        
        for i in range(len(info)):
            temp = deepcopy(info)
            temp[i] = "-"
            query = " ".join(temp)
            if query not in answer:
                answer[query] = [score]
            else:
                answer[query].append(score)
    return answer

def parsed_query(queries):
    answer = []
    for query in queries:
        query = query.replace(" and "," ")
        query = query.split()
        score = int(query.pop())
        answer.append([" ".join(query), score])
    return answer

def solution(info, query):
    answer = []
    info = parsed_info(info)
    
    for query, std_score in parsed_query(query):
        cnt = 0
        if query not in info:
            answer.append(cnt)
            continue
        for data_score in info[query]:
            if data_score >= std_score:
                cnt+=1
        answer.append(cnt)
    return answer