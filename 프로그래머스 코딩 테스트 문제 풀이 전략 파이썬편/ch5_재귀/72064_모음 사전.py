from itertools import product
def solution(word):
    mywords = []
    for i in range(1, 6):
        for myword in product("AEIOU", repeat = i):
            mywords.append("".join(myword))
    mywords.sort()
    return mywords.index(word)+1