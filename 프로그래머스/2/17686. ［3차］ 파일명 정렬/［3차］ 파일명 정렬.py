import re

def solution(files):
    answer = []

    pattern = re.compile(r"^([^0-9]+)([0-9]{1,5})(.*)$")
    for file in files:
        match = re.match(pattern, file)
        if match:
            answer.append(match.groups())

    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(i) for i in answer]