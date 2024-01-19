def make_partition(original, nums, partition=[]):
  result = []
  if sum(partition)==original:
    return partition
  for i in range(len(nums)):
    if sum(partition)+nums[i]==original:
      result.append(partition)
      result.append(make_partition(original, nums[:i]+nums[i+1:], partition+[nums[i]]))
  return result
    

def solution(n, nums):
  for i in range(max(nums), sum(nums)+1):
    if sum(nums)%i==0:
      return make_partition(i, nums)

n = int(input())
nums = list(map(int, input().split()))
print(solution(n, nums))