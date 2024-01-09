def solution(s):
    answer = ''
    
    idx = 0
    for a in s:
        if a==" ":
            answer+=a
            idx = 0
        else:
            if idx%2==0:
                answer+=a.upper()
            elif idx%2!=0:
                answer+=a.lower()
            idx+=1
    return answer