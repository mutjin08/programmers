def parse_date(date):
    y, m, d = map(int, date.split("."))
    return y*12*28+m*28+d #주의

def parse_terms(terms):
    dic = {}
    for term in terms:
        x, m = term.split()
        dic[x] = int(m)*28
    return dic

def solution(today, terms, privacies):
    today = parse_date(today)
    terms = parse_terms(terms)
    
    answer = []
    for i, privacy in enumerate(privacies):
        d, t = privacy.split()
        expday = parse_date(d) + terms[t]
        
        if today >= expday:
            answer.append(i+1)
    return answer