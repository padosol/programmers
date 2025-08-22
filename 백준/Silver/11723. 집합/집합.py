import sys
input = sys.stdin.readline
n = int(input())

S = 0
for _ in range(n):
    arr = input().strip().split()

    command = arr[0]

    # |: or 연산, ^: nor 연산, &: and 연산, ~: 보수 연산
    if command == 'add':
        S |= (1 << int(arr[1]))
    elif command == 'remove':
        S &= ~(1 << int(arr[1]))
    elif command == 'check':
        print(1 if S & (1 << int(arr[1])) else 0)
    elif command == 'toggle':
        check = S & (1 << int(arr[1]))
        if check:
            S ^= (1 << int(arr[1]))
        else:
            S |= (1 << int(arr[1]))
    elif command == 'all':
        S = (1 << 21) - 1
    elif command == 'empty':
        S = 0


