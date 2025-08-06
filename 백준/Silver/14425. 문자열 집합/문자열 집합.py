N, M = map(int, input().split())
S = set()
count = 0
for i in range(N):
    S.add(input())

for i in range(M):
    s = input()
    if s in S:
        count += 1

print(count)