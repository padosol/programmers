# 드래곤 커브의 개수
N = int(input())
curve_info = []

# 100 X 100
board = [[0 for _ in range(101)] for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    # x 좌표,
    # y 좌표
    # d 방향
    # g 세대수
    x, y, d, g = map(int, input().split())
    curve_info.append([x, y, d, g])

for curve in curve_info:
    # 0, 0 좌표로 옮기고 
    # 90도 회전 
    # 다시 원래 좌표로 이동
    x, y, d, g = curve
    q = [[y, x]]
    board[y][x] = 1

    # 0 세대는 무조건 있음
    # 0 세대 좌표 추가
    board[y+dy[d]][x + dx[d]] = 1
    q.append([y+dy[d], x+dx[d]])

    # 끝 점
    end_point = [y+dy[d], x+dx[d]]
    
    # q 에서
    for i in range(1, g + 1):
        size = len(q)
        for j in range(size):
            ny, nx = q[j]

            dny = (nx - end_point[1]) + end_point[0]
            dnx = -(ny - end_point[0]) + end_point[1]
            board[dny][dnx] = 1
            q.append([dny, dnx])

            if j == size-1:
                dny = (q[0][1] - end_point[1]) + end_point[0]
                dnx = -(q[0][0] - end_point[0]) + end_point[1]
                end_point = [dny, dnx]

answer = 0
for y in range(100):
    for x in range(100):
        if board[y][x] == 1 and board[y+1][x] == 1 and board[y][x+1] == 1 and board[y+1][x+1] == 1:
            answer += 1

print(answer)
