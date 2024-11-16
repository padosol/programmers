from collections import deque

# 보드의 크기
N = int(input())

# 보드 세팅
board = [[-1 for _ in range(N+1)] for _ in range(N+1)]

# 사과의 개수
K = int(input())

# 사과의 위치
apples = [list(map(int, input().split())) for _ in range(K)]

# 사과 세팅
for x, y in apples:
    board[x][y] = 0

# 방향 변환 횟수
L = int(input())
dict = {}

for i in range(L):
    t, d = input().split()
    dict[int(t)] = d

x = 1
y = 1

dx = 1
dy = 0

snake = deque([[1,1]])

answer = 0
for i in range(1, 10001):

    # 도착한 후 방향을 바꿈
    x += dx
    y += dy

    # 게임이 끝인지 확인
    if x == 0 or x > N or y == 0 or y > N:
        answer = i
        break
    if [y, x] in snake:
        answer = i
        break

    # 사과면 머리추가 아니면 맨뒤를 현재에 추가
    if board[y][x] == 0:
        board[y][x] = -1
        snake.append([y, x])
    else:
        snake.popleft()
        snake.append([y, x])

    if i in dict:
        direction = dict[i]
        if direction == "D":
            dx, dy = -dy, dx
        elif direction == "L":
            dx, dy = dy, -dx

print(answer)
