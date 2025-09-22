def solution(m, musicinfos):
    answer = ['(None)', 0]
    m = m.replace("C#", 'c')
    m = m.replace("D#", 'd')
    m = m.replace("F#", 'f')
    m = m.replace("G#", 'g')
    m = m.replace("A#", 'a')
    m = m.replace("B#", 'c')

    for music in musicinfos:
        start, end, title, code = music.split(",")
        start_time = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
        end_time = int(end.split(":")[0]) * 60 + int(end.split(":")[1])
        total = end_time - start_time

        code = code.replace("C#", 'c')
        code = code.replace("D#", 'd')
        code = code.replace("F#", 'f')
        code = code.replace("G#", 'g')
        code = code.replace("A#", 'a')
        code = code.replace("B#", 'c')

        size = len(code)
        if total > size:
            code = code * int(total // size) + code[:total % size]
        else:
            code = code[:total]

        if m in code:
            if total > answer[1]:
                answer = (title, total)

    return answer[0]