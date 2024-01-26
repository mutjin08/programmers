def can_learn(skill_tree, skill):
    target = []
    for s in skill_tree:
        if s in skill:
            target.append(s)
    target = "".join(target)
    if target == skill[:len(target)]:
        return 1
    return 0
    
    

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += can_learn(skill_tree, skill)
    return answer