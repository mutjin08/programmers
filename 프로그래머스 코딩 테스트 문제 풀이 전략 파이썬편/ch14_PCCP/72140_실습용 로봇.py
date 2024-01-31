def solution(command):
    direction = 0
    step = [[-1, 0],[0, 1],[1, 0],[0, -1]]
    for cmd in command:
        if cmd=="R":
            direction += 1
            if direction>3:
                direction-=4
        elif cmd=="L":
            direction -= 1
            if direction<0:
                direction+=4
        