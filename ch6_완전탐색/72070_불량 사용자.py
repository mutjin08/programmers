def solution(user_id, banned_id):
    cands = [[] for _ in range(len(banned_id))]
    
    for b in range(len(banned_id)):
        for g in range(len(user_id)):
            bid, gid = banned_id[b], user_id[g]

            if len(bid)!=len(gid):
                continue

            flag=0
            for i in range(len(bid)):
                if not(bid[i]=="*" or bid[i]==gid[i]):
                    flag = 1
                    break
            if flag:
                continue

            cands[b].append(gid)
            
    return cands