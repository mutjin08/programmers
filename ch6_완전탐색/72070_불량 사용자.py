from itertools import permutations

def is_banned(uid, bid):
    if len(uid)!=len(bid):
        return False
    for i in range(len(uid)):
        if bid[i]=="*" or bid[i]==uid[i]:
            continue
        return False
    return True

def solution(user_id, banned_id):
    answer = []
    for users in permutations(user_id, len(banned_id)):
        all_banned = 1
        for i in range(len(users)):
            if not is_banned(users[i], banned_id[i]):
                all_banned = 0
                break
        if all_banned and set(users) not in answer:
            answer.append(set(users))
    return len(answer)