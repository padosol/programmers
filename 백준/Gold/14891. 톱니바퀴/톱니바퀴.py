# 기어 리스트
gear = [list(map(int, list(input()))) for _ in range(4)]

# 회전 수
K = int(input())

# 회전 정보
rotate_info = [list(map(int, input().split())) for _ in range(K)]

# 기어 연결 정보
links = [[], [2], [1, 3], [2, 4], [3]]

def gear_rotate(arr):
    for i in range(4):
        d = arr[i]
        if d == 0:
            continue
        if d == -1:
            gear[i] = gear[i][1:8] + gear[i][0:1]
        else:
            gear[i] = gear[i][7:8] + gear[i][0:7]

def rotate(o_gear_n, s_gear_n, d):
    if o_gear_n > s_gear_n:
        if gear[o_gear_n-1][6] == gear[s_gear_n-1][2]:
            return [s_gear_n, 0]
        else:
            return [s_gear_n, d * -1]
    else:
        if gear[o_gear_n-1][2] == gear[s_gear_n-1][6]:
            return [s_gear_n, 0]
        else:
            return [s_gear_n, d * -1]

# 회전 정보 만큼 돌림
for gear_num, direction in rotate_info:
    q = [[gear_num, direction]]

    visited = [False for _ in range(5)]
    visited[gear_num] = True
    rotate_gear = [0 for _ in range(4)]
    rotate_gear[gear_num-1] = direction
    while q:
        # 기어 번호와 방향 가져옴
        g, d = q.pop()

        for next_gear in links[g]:
            if not visited[next_gear]:
                visited[next_gear] = True
                n_gear, n_d = rotate(g, next_gear, d)
                q.append([n_gear, n_d])
                rotate_gear[next_gear-1] = n_d

    # 회전
    gear_rotate(rotate_gear)

answer = 0
weight = [1, 2, 4, 8]
for i in range(4):
    answer += gear[i][0] * weight[i]

print(answer)
