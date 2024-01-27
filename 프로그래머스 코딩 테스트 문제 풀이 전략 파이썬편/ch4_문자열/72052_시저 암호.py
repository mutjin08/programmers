def solution(s, n):
    answer = ""
    for c in s:
        c = ord(c)
        if 65<=c<=90:
            c += n
            if c>90:
                c = 65 + (c-90) -1
        elif 97<=c<=122:
            c += n
            if c>122:
                c = 97 + (c-122) -1
        answer+=chr(c)
    return answer
        