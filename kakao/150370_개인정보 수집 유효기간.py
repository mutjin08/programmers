def parse_date(date):
    y, m, d = map(int, date.split("."))
    return y*12*28+m*28+d

def parse_terms(terms):
    dic = {}
    for term in terms:
        t, m = term.split()
        dic[t] = int(m)*28
    return dic

def solution(today, terms, privacies):
    answer = []
    
    terms = parse_terms(terms)
    today = parse_date(today)
    
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split()
        exp_date = parse_date(date) + terms[term]
        if today >= exp_date:
            answer.append(idx+1)
            
    return answer