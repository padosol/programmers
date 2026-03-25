
import bisect

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

n = int(input())
arr = list(map(int, input().split()))

for a in arr:
    index = bisect.bisect_left(nums, a)
    if index < N and nums[index] == a:
        print(1)
    else:
        print(0)
