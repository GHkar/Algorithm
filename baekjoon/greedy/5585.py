# 거스름돈

n = 1000 - int(input())
change = [500,100,50,10,5,1]

result = 0

for i in change :
    result += int(n / i)
    n %= i
    if n==0 : break

print(result)
