def solution(s):
    cands = []
    for cut in range(2, len(s)//2):
        std = s[:cut]
        cnt = 1
        cand = ""
        
        for i in range(cut, len(s), cut):
            if std==s[i:i+cut]:
                cnt+=1
            else:
                if cnt>1:
                    cand+=str(cnt)+std
                else:
                    cand+=std
                std = s[:cut]
                cnt = 1
        cands.append(len(cand))
        
        return min(cands)
                    
                