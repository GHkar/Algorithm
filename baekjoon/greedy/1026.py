# treasure

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))



sB = {s : i for i,s in enumerate(B)}
sB = dict(sorted(sB.items(),reverse = True))

A.sort()
sA = dict(zip(sB.values(), A))
sA = dict(sorted(sA.items()))

A = list(sA.values())



answer = 0
for i in range(N):
    answer += (A[i] * B[i])

print(answer)



# N = int(input())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))

# newA = A[:]
# newB = B[:]

# for i in range(N):
#     nowIndex = newB.index(max(newB))
#     newB[nowIndex] = -1

#     A[nowIndex] = min(newA)
#     newA[newA.index(min(newA))] = 101

# answer = 0
# for i in range(N):
#     answer += (A[i] * B[i])

# print(answer)

