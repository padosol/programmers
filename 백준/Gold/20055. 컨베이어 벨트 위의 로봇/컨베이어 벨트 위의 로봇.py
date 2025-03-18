from collections import deque

# 컨베이어 벨트 길이 N
# 내구도가 0 인 칸의 제한 수 K
N, K = map(int, input().split())

# 벨트 내구도
robots = deque([False for _ in range(N)])
belt = deque(list(map(int, input().split())))

count = 0
check = 0

while True:
    count += 1

    # 컨베이어 벨트 이동
    robots[-1] = False
    robots.rotate(1)
    robots[-1] = False

    belt.rotate(1)

    # 로봇이 존재하면 로봇 이동
    for i in range(N - 2, -1, -1):
        if robots[i]:
            if i < N - 1:
                if belt[i+1] > 0 and not robots[i+1]:
                    robots[i] = False
                    robots[i+1] = True
                    belt[i+1] -= 1

                    if belt[i+1] == 0:
                        check += 1

    # 로봇 올림
    if belt[0] > 0 and not robots[0]:
        robots[0] = True
        belt[0] -= 1

        if belt[0] == 0:
            check += 1

    if check >= K:
        break


print(count)