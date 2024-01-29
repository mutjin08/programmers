def parse_info(info):
    infos = {}
    for i in info:
        i = i.split()
        score = int(i.pop())
        infos[" ".join(i)] = score
        
        for j in range(4):
            temp = i[j]
            i[j] = "-"
            infos[" ".join(i)] = score
            i[j] = temp
    return infos

def solution(info, query):
    info = parse_info(info)
    return info
