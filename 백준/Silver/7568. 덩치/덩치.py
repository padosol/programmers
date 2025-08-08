n = int(input())
human = []
for i in range(n):
    arr = list(map(int, input().split()))
    human.append(arr)

ranks = [1] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if human[j][0] > human[i][0] and human[j][1] > human[i][1]:
            ranks[i] += 1


print(*ranks)