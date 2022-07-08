# 1이 될 때까지

N, K = map(int, input().split())

result = 0
while True :
    if N % K == 0 :
        N //= K
        result += 1
    else :
        N -= 1
        result += 1

    if N == 1 : break

print(result)

    
