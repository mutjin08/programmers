def solution(people, limit):
    people.sort()
    l, r = 0, len(people) - 1
    boat = 0
    while l<=r:
        if people[l] + people[r] <= limit : 
            boat += 1
            l += 1
            r -= 1
        elif people[l] + people[r] > limit : 
            boat += 1
            r -= 1
    return boat