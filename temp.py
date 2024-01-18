from collections import deque
def find_partition(original, cuts):
  answer = []
  cuts.sort()
  cuts = deque(cuts)

  # 잘리지 않은 막대기 제거
  while cuts and cuts[-1]==original:
    answer.append([cuts.pop()])

  return answer

def solution(n, cuts):
  for original in range(max(cuts), sum(cuts)+1):
    if sum(cuts)%original==0:
      return [[original]]+find_partition(original, cuts)


n = int(input())
cuts = list(map(int, input().split()))
print(solution(n, cuts))