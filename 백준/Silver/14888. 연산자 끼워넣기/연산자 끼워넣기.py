def recur(number, idx):
    global answer_max
    global answer_min
    if idx == N:
        answer_max = max(answer_max, number)
        answer_min = min(answer_min, number)
        return

    for i in range(4):
        if cals[i] != 0:
            cals[i] -= 1
            if i == 0:
                recur(number + numbers[idx], idx + 1)
            elif i == 1:
                recur(number - numbers[idx], idx + 1)
            elif i == 2:
                recur(number * numbers[idx], idx + 1)
            elif i == 3:
                # 음수를 양수로 나눌
                if number < 0 or numbers[idx] < 0:
                    recur(-(abs(number) // abs(numbers[idx])), idx + 1)
                else:
                    recur(number // numbers[idx], idx + 1)
            cals[i] += 1

N = int(input())
numbers = list(map(int, input().split()))

# 0 덧셈, 1 뺄셈, 2 곱셈, 3 나눗셈
cals = list(map(int, input().split()))

answer_max = -100000000
answer_min = 1000000000

for i in range(1, N):
    for j in range(4):
        if cals[j] != 0:
            cals[j] -= 1
            if j == 0:
                recur(numbers[0] + numbers[1], 2)
            elif j == 1:
                recur(numbers[0] - numbers[1], 2)
            elif j == 2:
                recur(numbers[0] * numbers[1], 2)
            elif j == 3:
                # 음수를 양수로 나눌
                if numbers[0] < 0 or numbers[1] < 0:
                    recur(-(abs(numbers[0]) // abs(numbers[1])), 2)
                else:
                    recur(numbers[0] // numbers[1], 2)
            cals[j] += 1

print(answer_max)
print(answer_min)