def solution(board, skill):
    answer = 0

    arr_sum = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    for s in skill:
        type = s[0]
        if type == 1:
            arr_sum[s[1]][s[2]] -= s[5]
            arr_sum[s[1]][s[4]+1] += s[5]

            arr_sum[s[3]+1][s[2]] += s[5]
            arr_sum[s[3]+1][s[4]+1] -= s[5]
        else:
            arr_sum[s[1]][s[2]] += s[5]
            arr_sum[s[1]][s[4]+1] -= s[5]

            arr_sum[s[3]+1][s[2]] -= s[5]
            arr_sum[s[3]+1][s[4]+1] += s[5]
    for i in range(len(arr_sum)-1):
        for j in range(len(arr_sum[0])-1):
            arr_sum[i][j+1] += arr_sum[i][j]

    for i in range(len(arr_sum)-1):
        for j in range(len(arr_sum[0])-1):
            arr_sum[i+1][j] += arr_sum[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += arr_sum[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer