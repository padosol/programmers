def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    video_len = int(video_len.split(":")[0]) * 60 + int(video_len.split(":")[1])
    pos = int(pos.split(":")[0]) * 60 + int(pos.split(":")[1])
    op_start = int(op_start.split(":")[0]) * 60 + int(op_start.split(":")[1])
    op_end = int(op_end.split(":")[0]) * 60 + int(op_end.split(":")[1])

    for command in commands:
        pos = processing(video_len, pos, op_start, op_end, command)

    if op_start <= pos <= op_end:
        pos = op_end

    return str(pos // 60).zfill(2) + ":" + str(pos % 60).zfill(2)


def processing(video_len, pos, op_start, op_end, command):
    if op_start <= pos <= op_end:
        pos = op_end

    if command == 'next':
        pos += 10
        if pos > video_len:
            pos = video_len
    elif command == 'prev':
        pos -= 10
        if pos < 0:
            pos = 0

    return pos