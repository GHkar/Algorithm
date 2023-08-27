# 두 배열의 원소 교체

# 입력
N, K = map(int, input().split( ))

A = list(map(int, input().split( )))
B = list(map(int, input().split( )))

# 정렬, A는 오름차, B는 내림차 순으로 정렬해줌
A.sort()
B.sort(reverse=True)

# K개에 맞춰 각 순서대로 서로 스왑
for k in range(K):
    if A[k] < B[k] : A[k], B[k] = B[k], A[k]
    else : break

print(sum(A))
