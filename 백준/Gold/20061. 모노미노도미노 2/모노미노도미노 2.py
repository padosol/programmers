from collections import deque

green_field = deque([[0 for _ in range(4)] for _ in range(6)])
blue_field = deque([[0 for _ in range(4)] for _ in range(6)])


def create_domino(index, x, y):
    if index == 1:
        return [[x, y]]
    elif index == 2:
        return [[x, y], [x, y+1]]
    elif index == 3:
        return [[x, y], [x+1, y]]


def rotate_90(index, x, y):
    if index == 1:
        return [1, y, (4 - x - 1)]
    elif index == 2:
        return [3, y, (4 - x - 1)]
    else:
        return [2, y, (4 - x - 1 - 1)]


block_count = int(input())
block_info = [list(map(int, input().split())) for _ in range(block_count)]


def process(index, y, field):
    global answer

    pointer = 0
    dominos = []
    while pointer < 6:
        dominos = create_domino(index, pointer, y)

        # 현재 라인에 블록이 들어가는지 확인
        count = 0
        for [xx, yy] in dominos:
            if field[xx][yy] == 0:
                count += 1
            else:
                break

        if count == len(dominos):
            next_count = 0
            for [xxx, yyy] in dominos:
                if 6 > xxx+1 >= 0 and field[xxx + 1][yyy] == 0:
                    next_count += 1
            if next_count == len(dominos):
                pointer += 1
            else:
                break
        else:
            break

    # block 놓기
    if len(dominos) > 0:
        for [x, y] in dominos:
            field[x][y] = 1

    # 3 ~ 6 칸 블럭 제거
    for i in range(2, 6):
        count = 0
        for j in range(4):
            if field[i][j] == 1:
                count += 1

        # 해당칸 블럭 제거
        if count == 4:
            answer += 1
            for j in range(4):
                field[i][j] = 0

            # 해당칸 부터 위에 있는 블럭들 전부 아래로 내림
            for j in range(i - 1, -1, -1):
                for r in range(4):
                    if field[j][r] == 1:
                        field[j][r] = 0
                        field[j + 1][r] = 1

    # 1,2 칸에 블럭이 있는 경우
    # 해당 칸 만큼 아래 블록 제거
    count = 0
    for i in range(2):
        for j in range(4):
            if field[i][j] == 1:
                count += 1
                break

    for i in range(count):
        field.pop()
        field.appendleft([0, 0, 0, 0])


answer = 0
for block in block_info:
    green_block = block
    blue_block = rotate_90(green_block[0],green_block[1],green_block[2])

    process(green_block[0], green_block[2], green_field)
    process(blue_block[0], blue_block[2], blue_field)


total_count = 0

for i in range(6):
    for j in range(4):
        if green_field[i][j] == 1:
            total_count += 1

        if blue_field[i][j] == 1:
            total_count += 1


print(answer)
print(total_count)