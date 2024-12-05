import sys
from collections import deque

# N 크기, M 나무수, K 년
N, M, K = map(int, input().split())
default_board = [[5] * N for _ in range(N)]
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    # 좌표: (y, x), z: 나무의 나이
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    trees[x-1][y-1].append(z)

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

answer = 0
for _ in range(K):

    # 봄 & 여름
    for j in range(N):
        for i in range(N):
            tree = trees[j][i]
            next_tree = deque([])
            death_tree = 0
            for z in tree:
                if default_board[j][i] >= z:
                    default_board[j][i] -= z
                    next_tree.append(z+1)
                else:
                    death_tree += z // 2
            trees[j][i] = next_tree
            default_board[j][i] += death_tree

    # 가을
    for j in range(N):
        for i in range(N):
            tree = trees[j][i]
            for z in tree:
                if z % 5 == 0:
                    for d in range(8):
                        ny = j + dy[d]
                        nx = i + dx[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            trees[ny][nx].appendleft(1)

    # 겨울
    for j in range(N):
        for i in range(N):
            default_board[j][i] += board[j][i]

for j in range(N):
    for i in range(N):
        if len(trees[j][i]) > 0:
            answer += len(trees[j][i])

print(answer)

