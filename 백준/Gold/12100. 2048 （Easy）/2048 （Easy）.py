import sys, copy

def rotate_90(m):
    M = len(m)
    tmp = [[0] * M for _ in range(M)]

    for r in range(M):
        for c in range(M):
            tmp[c][M-1-r] = m[r][c]

    return tmp


def push(board):
    for i in range(N):
        cursor = 0
        for j in range(1, N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = tmp

                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board[i][cursor] = tmp

    return board


def recur(idx, board):
    global answer
    if idx == 5:
        for j in board:
            for i in j:
                if i > answer:
                    answer = i
        return

    new_board = copy.deepcopy(board)
    board_90 = rotate_90(board)
    board_180 = rotate_90(board_90)
    board_270 = rotate_90(board_180)

    recur(idx + 1, push(new_board))
    recur(idx + 1, push(board_90))
    recur(idx + 1, push(board_180))
    recur(idx + 1, push(board_270))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0

recur(0, arr)
print(answer)