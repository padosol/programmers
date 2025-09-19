def right_str(p):
    count = 0
    for c in p:
        if c == "(":
            count += 1
        else:
            if count:
                count -= 1

    return count == 0

# 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
def divide(p):
    if not p:
        return p
    l = 0
    r = 0
    index = 0
    for i, c in enumerate(p):
        if c == '(':
            l += 1
        else:
            r += 1

        if l == r:
            index = i
            break

    u = p[:index + 1]
    v = p[index + 1:]
    if right_str(u):
        result = divide(v)
        u += result
    else:
        result = "("
        result += divide(v)
        result += ")"
        u = u[1:-1]
        for c in u:
            if c == '(':
                result += ')'
            else:
                result += '('
        u = result
    return u

def solution(p):
    answer = divide(p)
    return answer