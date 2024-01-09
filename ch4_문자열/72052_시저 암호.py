def solution(s, n):
    answer = ''
    for a in s:
        if a.isupper():
            a = ord(a)+n
            if a>90:
                a = 65 + (a-90) -1
            a = chr(a)
        elif a.islower():
            a = ord(a)+n
            if a>122:
                a = 97 + (a-122) -1
            a = chr(a)
        answer+=a
    return answer