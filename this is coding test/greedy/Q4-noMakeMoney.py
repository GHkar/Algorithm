# 그리디 - 만들 수 없는 금액

N = int(input())
coin = list(map(int, input().split()))
coin.sort()

result = 1

for c in coin:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if result < c:
        break
    result += c


print(result)
