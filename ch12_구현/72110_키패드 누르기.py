def distance(a, b):
    positions = {'1':[0,0],'2':[0,1],'3':[0,2],'4':[1,0],'5':[1,1],'6':[1,2],'7':[2,0],'8':[2,1],'9':[2,2],'*':[3,0],'0':[3,1],'#':[3,2]}
    return abs(positions[a][0] - positions[b][0])+abs(positions[a][1] - positions[b][1])

def find_closer_hand(target, left_number, right_number):
    left_distance, right_distance = distance(target, left_number), distance(target, right_number)
    if left_distance < right_distance:
        return "left"
    elif left_distance > right_distance:
        return "right"
    else:
        return None

def solution(numbers, hand):
    answer = ''
    left_number, right_number = "*","#"
    for target in numbers:
        target = str(target)
        if target in ['1', '4', '7', '*']:
            answer+="L"
            left_number = target
        elif target in ['3', '6', '9', '#']:
            answer+="R"
            right_number = target
        else:
            closer_hand = find_closer_hand(target, left_number, right_number)
            if closer_hand=="left":
                answer+="L"
                left_number = target
            elif closer_hand=="right":
                answer+="R"
                right_number = target
            else:
                if hand=="left":
                    answer+="L"
                    left_number = target
                elif hand=="right":
                    answer+="R"
                    right_number = target
    return answer