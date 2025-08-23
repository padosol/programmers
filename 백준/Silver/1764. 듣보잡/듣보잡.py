n, m = map(int, input().split())

names = dict()
for i in range(n):
    name = input()
    names[name] = 0

answer = []
for j in range(m):
    name = input()
    if name in names:
        answer.append(name)

answer.sort()
size = len(answer)
print(size)
for n in answer:
    print(n)