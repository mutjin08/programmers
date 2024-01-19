def id_to_name(logs, users):
    for i in range(len(logs)):
        logs[i][0] = users[logs[i][0]]
        logs[i] = "".join(logs[i])
    return logs

def solution(record):
    answer = []
    users = {}
    for r in record:
        r = r.split()
        if len(r) == 3:
            user_action, user_id, user_name = r
        elif len(r) == 2:
            user_action, user_id = r
            
        if user_action=="Enter":
            answer.append([user_id, "님이 들어왔습니다."])
            users[user_id] = user_name
        elif user_action=="Change":
            users[user_id] = user_name
        elif user_action == "Leave":
            answer.append([user_id, "님이 나갔습니다."])
            
    return id_to_name(answer, users)