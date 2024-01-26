def solution(genres, plays):
    albums = {}
    counts = {}
    numbers = [i for i in range(len(genres))]
    for g, p, n in zip(genres, plays, numbers):
        if g not in albums:
            albums[g] = []
            counts[g] = 0
        albums[g].append([n, p])
        counts[g] += p
    
    answer = []
    for g, c in sorted(counts.items(), key = lambda x : -x[1]):
        albums[g].sort(key = lambda x : -x[1])
        if len(albums[g])<2:
            answer.append(albums[g][0][0])
        elif len(albums[g])>=2:
            answer.append(albums[g][0][0])
            answer.append(albums[g][1][0])
    return answer