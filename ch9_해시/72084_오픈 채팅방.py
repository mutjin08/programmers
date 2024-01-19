def id_to_name(logs, users):
    for i in range(len(logs)):
        logs[i][0] = users[logs[i][0]]
        logs[i] = "".join(logs[i])
    return logs
    

def solution(record):
    answer = []
    users = {}
    for r in record:
        temp = r.split()
        if len(temp)==3:
            action, user_id, user_name = temp
        elif len(r)==2:
            action, user_id = temp
        
        if action == "Enter":
            users[user_id] = user_name
            answer.append([user_id,"님이 나갔습니다."])
        elif action == "Leave":
            answer.append([user_id,"님이 들어왔습니다."])
        elif action == "Change":
            users[user_id] = user_name
    
    return id_to_name(answer, users)