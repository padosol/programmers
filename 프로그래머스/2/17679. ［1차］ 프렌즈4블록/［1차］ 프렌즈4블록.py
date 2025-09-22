def solution(m, n, board):
    answer = 0

    while True:
        remove_block = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != "#" and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove_block.add((i, j))
                    remove_block.add((i, j+1))
                    remove_block.add((i+1, j))
                    remove_block.add((i+1, j+1))

        if not remove_block:
            break

        answer += len(remove_block)
        for i, j in remove_block:
            board[i] = board[i][:j] + "#" + board[i][j+1:]

        for i in range(m - 1, -1, -1):
            for j in range(n):
                if board[i][j] == '#':
                    index = i
                    point = i
                    while index > 0:
                        index -= 1
                        if board[index][j] == '#':
                            continue

                        board[point] = board[point][:j] + board[index][j] + board[point][j + 1:]
                        board[index] = board[index][:j] + "#" + board[index][j + 1:]

                        point -= 1
    return answer