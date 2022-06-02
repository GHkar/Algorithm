# ATM


n = int(input())
p = list(map(int,input().split()))

p.sort()
n = 0
answer = 0

for t in p:
    n += t
    answer +=n

print(answer)
