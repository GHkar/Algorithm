# 개수
N = input()

# 무게 추
weight = list(map(int, input().split()))

# 무게 추 정렬
weight.sort()

# 양의 정수로 설정
answer = 1

for w in weight:
    if answer < w :
        break
    answer += w

print(answer)
