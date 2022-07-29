# 계단 오르기

n = int(input())

point = [0]

for i in range(n):
    point.append(int(input()))

dp = [[0,0]] * (n+1)
if n >= 1 :
    dp[1] = [0,point[1]]
if n >=2 :
    dp[2] = [point[2], point[1]+point[2]]

if n >= 3:
    for i in range(3, n):
        dp[i] = [point[i] + max(dp[i-2]), point[i]+ dp[i-1][0]]


if n <= 2 :
    print(dp[n][1])
else :
    print(point[n] + max([dp[n-1][0]] + dp[n-2]))
