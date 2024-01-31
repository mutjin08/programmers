def solution(command):
    answer = [0, 0]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    d = 0
    for c in command:
        if c=="R":
            d = (d+1)%4
        if c=="L":
            d = (d+3)%4
        if c=="G":
            answer[0] += move[d][0]
            answer[1] += move[d][1]
        if c=="B":
            answer[0] -= move[d][0]
            answer[1] -= move[d][1]
    return answer