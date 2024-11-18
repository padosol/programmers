n = int(input())
numbers = sorted(list(map(int, input().split())))
x = int(input())

lp = 0
rp = len(numbers) - 1

answer = 0
while lp < rp:
    sum = numbers[lp] + numbers[rp]

    if sum == x:
        answer += 1
        lp += 1
        rp -= 1
    elif sum < x:
        lp += 1
    else:
        rp -= 1

print(answer)


