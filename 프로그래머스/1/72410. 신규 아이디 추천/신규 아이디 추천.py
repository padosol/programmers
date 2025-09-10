import re

def solution(new_id):
    # 모든 대문자를 소문자로 치환합니다.
    new_id = new_id.lower()

    # 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자를 제거합니다.
    pattern = r'[^a-z0-9\-_.]'
    new_id = re.sub(pattern, '', new_id)

    # 마침표가 2번이상 연속된 부분을 하나의 마침표로 치환합니다.
    pattern2 = r'\.{2,}'
    new_id = re.sub(pattern2, '.', new_id)


    # 마침표가 처음이나 끝에 위치한다면 제거합니다.
    new_id = new_id.strip(".")

    # 빈문자열이라면, a 를 대입합니다.
    if not new_id:
        new_id = 'a'

    # 길이가 16자 이상이면 첫 15개를 제외한 나머지를 제거합니다. 만약 제거후 마침표가 끝에있다면 끝에위치한 마침표를 제거합니다.
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id[:14]

    # 길이자 2자 이하라면 문자열의 길이자 3이 될때까지 반복합니다.
    if len(new_id) < 3:
        while len(new_id) != 3:
            new_id += new_id[-1]

    return new_id