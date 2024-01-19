def make_partition(original, nums, partitions = []):
  if sum(partitions)==original:
    return [partitions]
  
  for i in range(len(nums)):
    if sum(partitions)+nums[i]==original:
      return make_partition(original, nums[:i]+nums[i+1:], partitions+[nums[i]])
    

def solution(nums):
  for i in range(max(nums), sum(nums)+1):
    if sum(nums)%i==0:
      return make_partition(i, nums)

n = int(input())
nums = list(map(int, input().split()))
print(solution(nums))