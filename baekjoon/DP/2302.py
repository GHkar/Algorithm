# 극장 좌석

N = int(input())
M = int(input())

vip = []
for i in range(M) :
    vip.append(int(input()))

dp = [1, 1, 2]
for i in range(3, N+1):
    dp.append(dp[i-1] + dp[i-2])

answer = []

# vip를 기준으로 좌석 자르기
count = 0
for i in range(1, N+1):
    if i in vip :
        answer.append(dp[count])
        count = 0
    else:
        count += 1
answer.append(dp[count])  # 마지막     

# answer에 있는 모든 요소 곱하기
print(eval("*".join([str(n) for n in answer])))

