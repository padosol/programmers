import copy

def recur(idx, arr, d):
    global cctv
    global cctv_direction
    global answer
    cctv_num, j, i = cctv[idx]
    next_arr = copy.deepcopy(arr)

    if cctv_num != 0:
        # 계산
        directions = cctv_direction[cctv_num]
        for dy, dx in directions[d]:
            ny = j
            nx = i
            while True:
                ny += dy
                nx += dx
                if 0 <= ny < N and 0 <= nx < M:
                    if next_arr[ny][nx] == 6:
                        break

                    if next_arr[ny][nx] == 0:
                        next_arr[ny][nx] = -1

                else:
                    break

    if idx+1 == len(cctv):
        count = 0
        for y in range(N):
            for x in range(M):
                if next_arr[y][x] == 0:
                    count += 1
        answer = min(answer, count)
        return

    next_cctv, nj, ni = cctv[idx+1]
    if next_cctv == 1 or next_cctv == 3 or next_cctv == 4:
        recur(idx + 1, copy.deepcopy(next_arr), 0)
        recur(idx + 1, copy.deepcopy(next_arr), 1)
        recur(idx + 1, copy.deepcopy(next_arr), 2)
        recur(idx + 1, copy.deepcopy(next_arr), 3)
    elif next_cctv == 2:
        recur(idx + 1, copy.deepcopy(next_arr), 0)
        recur(idx + 1, copy.deepcopy(next_arr), 1)
    else:
        recur(idx + 1, copy.deepcopy(next_arr), 0)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cctv = [[0,0,0]]
for j in range(N):
    for i in range(M):
        if 1 <= board[j][i] <= 5:
            ## cctv 번호와 좌표 저장
            cctv.append([board[j][i], j, i])

cctv_direction = {
    1: [
        [[1, 0]],
        [[-1, 0]],
        [[0, 1]],
        [[0, -1]]
    ],
    2: [
        [[1, 0], [-1, 0]],
        [[0, 1], [0, -1]]
    ],
    3: [
        [[1, 0], [0, 1]],
        [[0, 1], [-1, 0]],
        [[-1, 0], [0, -1]],
        [[0, -1], [1, 0]]
    ],
    4: [
        [[0, 1], [1, 0], [0, -1]],
        [[1, 0], [0, -1], [-1, 0]],
        [[0, -1], [-1, 0], [0, 1]],
        [[-1, 0], [0, 1], [1, 0]]
    ],
    5: [
        [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ]
}

answer = 999999999
recur(0, copy.deepcopy(board), 0)
print(answer)

