# RGB 거리

N = int(input())

cost = []

# 입력 받기
for i in range(N):
    cost.append(list(map(int, input().split(' '))))

# DP 계산하기
for i in range(1, N):
    cost[i][0] = cost[i][0] + min(cost[i-1][1], cost[i-1][2])
    cost[i][1] = cost[i][1] + min(cost[i-1][0], cost[i-1][2])
    cost[i][2] = cost[i][2] + min(cost[i-1][0], cost[i-1][1])

# 결과 출력
print(min(cost[N-1]))
