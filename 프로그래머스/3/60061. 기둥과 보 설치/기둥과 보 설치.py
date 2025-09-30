def check_validity(n, frame):
    for x, y, a in frame:

        if a == 0:
            is_valid = (y == 0)
            is_valid |= (x - 1, y, 1) in frame
            is_valid |= (x, y, 1) in frame
            is_valid |= (x, y - 1, 0) in frame

            if not is_valid:
                return False

        else:  # a == 1
            is_valid = (x, y - 1, 0) in frame
            is_valid |= (x + 1, y - 1, 0) in frame

            is_valid |= ((x - 1, y, 1) in frame and (x + 1, y, 1) in frame)

            if not is_valid:
                return False

    return True  # 모든 구조물이 유효함

def solution(n, build_frame):
    frame = set()

    for x, y, a, b in build_frame:
        item = (x, y, a)

        if b == 1:  # 설치
            frame.add(item)

            if not check_validity(n, frame):
                frame.remove(item)

        else:  # 삭제
            if item in frame:
                frame.remove(item)

                if not check_validity(n, frame):
                    frame.add(item)

    result = [list(item) for item in frame]

    result.sort(key=lambda x: (x[0], x[1], x[2]))

    return result