def recur(n):
  for i in range(1, 44):
    for j in range(1, 44):
      for k in range(1, 44):
        if prefix[i] + prefix[j] + prefix[k] == num:
          return 1
  return 0

N = int(input())

nums = [int(input()) for _ in range(N)]

prefix = [0 for _ in range(44 + 1)]
for i in range(1, 44):
  prefix[i] = prefix[i-1] + i

for num in nums:
  print(recur(num))