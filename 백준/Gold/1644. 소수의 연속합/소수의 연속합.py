N = int(input())

if N == 1:
    print(0)
    exit(0)

prime_number = [True] * (N + 1)

def make_prime_number():
    prime_number[0] = False
    prime_number[1] = False

    arr = []
    for i in range(2, N + 1):
        if prime_number[i]:
            arr.append(i)
            for j in range(2, N // i + 1):
                prime_number[i * j] = False

    return arr

arr = make_prime_number()

left, right = 0, 0

total = arr[0]
cnt = 0
while left <= right:
    if total <= N:
        if total == N:
            cnt += 1

        right += 1
        if right == len(arr):
            break 

        total += arr[right]

    elif N < total:
        total -= arr[left]
        left += 1

print(cnt)
