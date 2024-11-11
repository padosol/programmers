N = int(input())

answer = 0
for i in range(1, 1000001):
  num = i + sum(list(map(int, str(i))))
  if num == N:
    answer = i
    break
    
print(answer)