# 정수 삼각형

n = int(input())

triangle = []
dp = [[] * 1 for i in range(n-1)]

for i in range(n):
    triangle.append(list(map(int, input().split(' '))))

dp.append(triangle[n-1])

for i in range(n-2, -1, -1):
    for j in range(len(triangle[i])) :
        dp[i].append(triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1]))

print(dp[0][0])
