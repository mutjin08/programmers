def solution(new_id):
    #1단계
    ans = new_id.lower()
    
    #2단계
    temp = ""
    for a in ans:
        if a.isalnum() or a in "-_.":
            temp+=a
    ans = temp
    
    #3단계(주의)
    while ".." in ans:
        ans = ans.replace("..",".")
    
    #4단계
    ans = ans.strip(".")
    
    #5단계
    if len(ans)<1:
        ans = "a"
        
    #6단계
    if len(ans)>=16:
        ans = ans[:15]
    ans = ans.rstrip(".")
    
    #7단계
    if len(ans)==1:
        ans = ans*3
    elif len(ans)==2:
        ans = ans[0]+ans[1]*2
    
    return ans