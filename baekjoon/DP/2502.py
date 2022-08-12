# 떡 먹는 호랑이

D, K = map(int, input().split(' '))

dp = [0 * 1 for i in range(D)]


for first in range(1, 100000):
    for second in range(1, 100000):
        dp[0] = first
        dp[1] = second

        for i in range (2, D):
            dp[i] = dp[i-1] + dp[i-2]

        if dp[D-1] >= K : break
    if dp[D-1] == K : break

print(first)
print(second)   

