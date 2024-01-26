def solution(citations):
    h = max(citations)
    
    
    # h==0인 경우 주의
    while h>=0:
        cited = 0
        for c in citations:
            if c>=h:
                cited+=1
        if cited>=h:
            return h
        h -= 1
            