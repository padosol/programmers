S = input()
answer = set()
size = len(S)
for i in range(size):
    for j in range(i, size):
        answer.add(S[i:j+1])
print(len(answer))