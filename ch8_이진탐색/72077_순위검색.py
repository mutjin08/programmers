def parsed_info(infos):
    answer = {}
    for info in infos:
        info = info.split()
        score = int(info.pop())
        query = " ".join(info)
        if query not in answer:
            answer[query] = [score]
        else:
            answer[query].append(score)
    return answer

def parsed_query(query):
    answer = []
    for q in query:
        q = q.replace(" and "," ")
        q = q.split()
        score = int(q.pop())
        answer.append([" ".join(q), score])
    return answer

def solution(info, query):
    query = parsed_query(query)
    info = parsed_info(info)
    return info