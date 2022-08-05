# 카드 구매하기
n = int(input())

card = list(map(int, input().split(' '))) 

dp = [0] * n
dp[0] = card[0]
dp[1] = max(card[0] + dp[0], card[1])

for i in range(2, n, 1) :
    dp[i] = max(dp[i-1] + card[0], card[i])

    # 예외 구하기
    for j in range(1,i):
        if j > i-1-j : break
        dp[i] = max(dp[i], dp[j] + dp[i-1-j])

print(dp[n-1])
