from itertools import permutations
def solution(ability):
    answer = []
    people = len(ability)
    sport = len(ability[0])
    for case in permutations(range(people), sport):
        answer.append(sum([ability[case[i]][i] for i in range(sport)]))
    return max(answer)