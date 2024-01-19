from collections import deque

def make_partition(n, lengths, partition=[]):
    if sum(partition) == n:
        return [partition]

    partitions = []
    for length in lengths:
        remaining_lengths = [l for l in lengths if l != length]
        if sum(partition) + length <= n:
            new_partition = partition + [length]
            partitions += make_partition(n, remaining_lengths, new_partition)

    return partitions

def find_partition(original, cuts):
  answer = []
  cuts.sort()
  cuts = deque(cuts)

  # 잘리지 않은 막대기 제거
  while cuts and cuts[-1]==original:
    answer.append([cuts.pop()])
  if not cuts:
    return answer

  # 잘린 막대기 제거
  return answer+make_partition(original, cuts)

def solution(n, cuts):
  for original in range(max(cuts), sum(cuts)+1):
    if sum(cuts)%original==0:
      return [[original]]+find_partition(original, cuts)


n = int(input())
cuts = list(map(int, input().split()))
for s in (solution(n, cuts)):
  print(*s)