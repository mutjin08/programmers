from collections import deque
def solution(tickets):
    tickets.sort(key = lambda x : (x[0], x[1]))
    q = deque([[["ICN"], tickets]])
    
    while q:
        now_paths, now_tickets = q.popleft()
        
        if len(now_tickets) == 0:
            return now_paths
        
        valid_idx = -1
        for i in range(len(now_tickets)):
            if now_tickets[i][0] == now_paths[-1]:
                valid_idx = i
                break
        
        if valid_idx == -1:
            continue
        
        while valid_idx < len(now_tickets) and now_tickets[valid_idx][0] == now_paths[-1]:
            # 주의 1 : now_paths, now_tickets 재사용되어야 해서 건들노
            q.append([now_paths+[now_tickets[valid_idx][1]], now_tickets[:valid_idx]+now_tickets[valid_idx+1:]])
            valid_idx += 1 #주의 2 : 계속 키워줘야됨