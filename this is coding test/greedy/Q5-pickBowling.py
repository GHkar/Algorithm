# 그리디 - 볼링공 고르기

N, M = map(int, input().split())
boaling = list(map(int, input().split()))
answer = [0] * (M + 1)
result = 0

# 각 무게 별 개수를 셈
for b in boaling :
    answer[b] += 1

# 1번 볼링공부터, 총 개수에서 본인의 개수만큼 빼고, 뺀 값에 본인의 개수만큼 곱해서, 최종 값에 더하기
for a in answer[1:]:
    N -= a
    result += (N * a)


print(result)
