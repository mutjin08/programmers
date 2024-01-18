from collections import deque
def make_partition(original, cuts, partition = []):
  

  return [[-1]]

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
  answer.append(make_partition(original, cuts))
  return answer

def solution(n, cuts):
  for original in range(max(cuts), sum(cuts)+1):
    if sum(cuts)%original==0:
      return [[original]]+find_partition(original, cuts)


n = int(input())
cuts = list(map(int, input().split()))
for s in (solution(n, cuts)):
  print(*s)