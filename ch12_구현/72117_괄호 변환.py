def make_balanced(target):
    l, r = 0, 0
    for i in range(len(target)):
        if target[i]=="(":
            l+=1
        elif target[i]==")":
            r+=1
        if l==r:
            return target[:i+1], target[i+1:]
    
    return target, ""

def is_balanced(target):
    # 예외처리
    if len(target)%2!=0:
        return False
    
    if target.count('(')==target.count(')'):
        return True
    return False

def is_correct(target):
    # 예외처리
    if target[0]==")" or target[-1]=="(":
        return False
    
    if not is_balanced(target):
        return False

    cnt = 0
    for c in target:
        if c=="(":
            cnt += 1
        elif c==")":
            if cnt<1:
                return False
            elif cnt>=1:
                cnt -= 1
    if cnt>0:
        return False
    return True
        

def solution(w):
    if len(w)==0:
        return ""
    u, v = make_balanced(w)
    if is_correct(u):
        return u+solution(v)
    
    u = "".join(reversed(u[1:len(u)-1]))
    return "("+solution(v)+")"+u