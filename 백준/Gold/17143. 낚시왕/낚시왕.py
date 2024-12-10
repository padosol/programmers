# R X C, M 상어수
import sys
R, C, M = map(int, input().split())

sharks = [[[] for _ in range(C)] for _ in range(R)]

human = 0
for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    sharks[r - 1][c - 1].append([s, d, z])

total_shark = 0

r_cycle = 2 * (R-1)
c_cycle = 2 * (C-1)

dx = [0, 0, 0, 1, -1]
dy = [0, -1, 1, 0, 0]
while human < C:
    # 낚시왕이 오른쪽으로 이동

    # 낚시 왕이 낚시
    for i in range(R):
        if len(sharks[i][human]) > 0:
            total_shark += sharks[i][human][0][2]
            sharks[i][human] = []
            break

    # 상어 이동
    # 방향 전환이 관건
    new_shark = [[[] for _ in range(C)] for _ in range(R)]
    for j in range(R):
        for i in range(C):
            # 속도, 방향, 크기
            for s, d, z in sharks[j][i]:
                fy = j
                fx = i
                direction = d
                if d == 3:
                    move = s + i
                    next_move = move % c_cycle
                    if next_move < c_cycle/2:
                        fx = next_move
                        direction = 3
                    else:
                        fx = c_cycle - next_move
                        direction = 4
                elif d == 4:
                    move = s - i
                    next_move = move % c_cycle
                    if next_move < c_cycle/2:
                        fx = next_move
                        direction = 3
                    else:
                        fx = c_cycle - next_move
                        direction = 4
                elif d == 1:
                    move = s - j
                    next_move = move % r_cycle
                    if next_move > r_cycle/2:
                        fy = r_cycle - next_move
                        direction = 1
                    else:
                        fy = next_move
                        direction = 2
                elif d == 2:
                    move = s + j
                    next_move = move % r_cycle
                    if next_move > r_cycle/2:
                        fy = r_cycle - next_move
                        direction = 1
                    else:
                        fy = next_move
                        direction = 2

                new_shark[fy][fx].append([s, direction, z])

    # 상어 서열정리
    for j in range(R):
        for i in range(C):
            if len(new_shark[j][i]) > 1:
                king_shark = sorted(new_shark[j][i], key=lambda x: -x[2])[0]
                new_shark[j][i] = [king_shark]

    sharks = new_shark
    human += 1

print(total_shark)

