import copy
from collections import deque
N, M = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

virus = []
selected_virus = []
for j in range(N):
    for i in range(N):
        if room[j][i] == 2:
            virus.append([j, i])
            room[j][i] = -2
        elif room[j][i] == 1:
            room[j][i] = -1


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 999999999


def recur(index):
    global answer

    if len(selected_virus) == M:

        q = deque([])
        tmp_room = copy.deepcopy(room)

        for [sv_j, sv_i] in selected_virus:
            q.append([sv_j, sv_i])
            tmp_room[sv_j][sv_i] = -3

        time = 0
        while q:
            length = len(q)
            for _ in range(length):
                vy, vx = q.popleft()

                for d in range(4):
                    nx = vx + dx[d]
                    ny = vy + dy[d]

                    if 0 <= nx < N and 0 <= ny < N:
                        if tmp_room[ny][nx] == 0:
                            if tmp_room[vy][vx] == -3:
                                tmp_room[ny][nx] = 1
                            else:
                                tmp_room[ny][nx] = tmp_room[vy][vx] + 1
                            time = max(time, tmp_room[ny][nx])
                            q.append([ny, nx])

                        if tmp_room[ny][nx] == -2:
                            if tmp_room[vy][vx] == -3:
                                tmp_room[ny][nx] = 1
                            else:
                                tmp_room[ny][nx] = tmp_room[vy][vx] + 1

                            q.append([ny, nx])

        for jjj in range(N):
            for iii in range(N):
                if tmp_room[jjj][iii] == 0:
                    return

        answer = min(answer, time)

        return

    for idx in range(index, len(virus)):
        selected_virus.append(virus[idx])
        recur(idx+1)
        selected_virus.remove(virus[idx])


for i in range(len(virus)):
    selected_virus.append(virus[i])
    recur(i+1)
    selected_virus.remove(virus[i])

if answer == 999999999: answer = -1

print(answer)