# 팀 결성

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 경로 압축 기법 / 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
N, M = map(int, input().split())
parent = [0] * (N + 1)  # 부모 테이블 초기화

# 부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(1, N + 1):
    parent[i] = i

result = []

for i in range(M):
    c, a, b = map(int, input().split())
    # 합치기 연산인 경우
    if c == 0:
        union_parent(parent, a, b)
    # 찾기 연산인 경우
    else :
        if find_parent(parent, a) == find_parent(parent, b):
            result.append('YES')
        else : result.append('NO')

for r in result:
    print(r)

