import copy
from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def poison():
    global answer
    q = deque()
    copy_board = copy.deepcopy(board)

    for j in range(N):
        for i in range(M):
            if copy_board[j][i] == 2:
                q.append((j, i))

    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if copy_board[ny][nx] == 0:
                    copy_board[ny][nx] = 2
                    q.appendleft((ny, nx))

    count = 0
    for y in range(N):
        for x in range(M):
            if copy_board[y][x] == 0:
                count += 1

    answer = max(answer, count)

def recur(idx):
    if idx == 3:
        poison()
        return

    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                board[y][x] = 1
                recur(idx + 1)
                board[y][x] = 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0
recur(0)

print(answer)





