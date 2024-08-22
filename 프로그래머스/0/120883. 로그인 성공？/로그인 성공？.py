def solution(id_pw, db):
    answer = 'fail'

    for i in db:
        if i[0] == id_pw[0]:
            answer = 'wrong pw'
            if i[1] == id_pw[1]:
                answer = 'login'


    return answer