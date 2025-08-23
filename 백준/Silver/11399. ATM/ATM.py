n = int(input())
human = list(map(int, input().split()))
human.sort()

answer = 0
for i in range(n):
    answer += sum(human[:i+1])

print(answer)