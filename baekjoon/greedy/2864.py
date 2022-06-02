# 5와 6의 차이

A, B = map(list, input().split())

minA = A[:]
maxA = A[:]
minB = B[:]
maxB = B[:]

num = 0
for a in A:
    if a == '5':
        maxA[num] = '6'
    elif a == '6':
        minA[num] = '5'
    num += 1

num = 0
for b in B:
    if b == '5':
        maxB[num] = '6'
    elif b == '6':
        minB[num] = '5'
    num += 1


print(int(''.join(map(str, minA))) + int(''.join(map(str, minB))), end = ' ')
print(int(''.join(map(str, maxA))) + int(''.join(map(str, maxB))))
