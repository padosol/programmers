# 시험장의 개수
N = int(input())

# 응시자 수
a_list = list(map(int, input().split()))

# 총 감독관이 감독할 수 있는 응시자 수 B
# 부 감독관이 감독할 수 있는 응시자 수 C
B, C = map(int, input().split())

answer = 0
for i in a_list:

    num = i - B

    # 총 감독관으로 처리 가능한 경우
    if num < 1:
        answer += 1
        continue
        
    # 총 감독관 + 부감독관으로 처리 가능한 경우
    if num - C < 1:
        answer += 2
        continue

    num_1 = num - C

    if num_1 % C == 0:
        answer += 2 + num_1 // C
    else:
        answer += 2 + num_1 // C + 1


print(answer)