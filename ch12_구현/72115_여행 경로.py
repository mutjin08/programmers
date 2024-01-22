from collections import deque

def solution(tickets):
    tickets.sort(key = lambda x : (x[0], x[1]))
    q = deque(["ICN", tickets])
    
    while q:
        now_paths, now_tickets = q.popleft()
        
        if not now_tickets:
            return now_paths
        
        idx = -1
        for i in range(len(now_tickets)):
            if now_tickets[i][0] == now_paths[-1]:
                idx = i
                break
        
        if idx == -1:
            continue
            
        while idx<=len(now_tickets) and now_tickets[idx][0] == now_paths[-1]:
            now_paths.append(now_tickets.pop(idx)[1])
            q.append([now_paths, now_tickets])
    return tickets