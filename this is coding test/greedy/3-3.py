# 가장 큰 수 찾기
n, m = map(int, input().split())

result = 0
for i in range(n):
    minvalue = min(list(map(int, input().split())))
    result = max(result, minvalue)

print(result)
