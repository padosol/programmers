def checking(list):
    global answer
    for j in range(N):
        target = 0
        count = L
        success = True
        for i in range(N):
            if list[j][i] > target:
                if abs(list[j][i] - target) != 1 and target != 0:
                    success = False
                    break
                if count < L:
                    success = False
                    break
                target = list[j][i]
                count = 0
            elif list[j][i] < target:
                if abs(list[j][i] - target) != 1 and target != 0:
                    success = False
                    break
                if count < 0:
                    success = False
                    break
                target = list[j][i]
                count = -L

            count += 1

            if i == N - 1:
                if count < 0:
                    success = False
        if success:
            answer += 1

def rotate_90(arr):
    tmp_arr = [[0] * N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            tmp_arr[N-1-i][j] = arr[j][i]

    return tmp_arr


N, L = map(int, input().split())

datas = [list(map(int, input().split())) for _ in range(N)]

answer = 0
checking(datas)
checking(rotate_90(datas))

print(answer)
