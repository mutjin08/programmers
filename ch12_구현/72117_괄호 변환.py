#주의 : 문자를 뒤집는거야 순서 거꾸로가 아니라
def is_correct(w):
    cnt = 0
    for c in w:
        if c=="(":
            cnt += 1
        elif c==")":
            if cnt==0:
                return False
            else:
                cnt -= 1
    if cnt==0:
        return True
    return False

def make_balanced(w):
    l, r = 0, 0
    for i in range(len(w)):
        if w[i]=="(":
            l+=1
        elif w[i]==")":
            r+=1
        
        if l==r:
            return w[:i+1], w[i+1:]

def solution(w):
    if len(w)==0:
        return ""
    
    u, v = make_balanced(w)
    
    if is_correct(u):
        return u+solution(v)
    
    temp = ""
    for c in u[1:len(u)-1]:
        if c=="(":
            temp+=")"
        elif c==")":
            temp+="("
    
    return "("+solution(v)+")"+temp