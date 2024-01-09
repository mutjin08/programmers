def solution(s):
    if len(s)%2!=0:
        return 0
    
    while len(s)>1:
        removed = 0
        for i in range(1, len(s)):
            if s[i-1]==s[i]:
                if i==len(s)-1:
                    s = s[:i-1]
                else:
                    s = s[:i-1]+s[i+1:]
                removed = 1
                break
        if removed:
            continue
        else:
            return 0
    return 1