# 섬 연결하기 - 유니온 파인드

# 1. 유니온 파인드 구현
# 부모 노드 반환
def find(parent, x):
    if parent[x] == x: return x
    parent[x] = find(parent, parent[x])
    return parent[x]

# 순환 방지 및 새롭게 부모 노드 지정
def union(parent, x,  y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y : return
    parent[x] = y

def solution(n, costs):
    # 2. 간선 비용이 적은 순서대로 정렬
    answer = cnt = 0
    parent = [i for i in range(n)]
    costs = sorted(costs, key=lambda x:x[2])

    # 3. 유니온 파인드의 성질을 이용하여 섬을 연결 (중복을 방지해서 최소 비용으로 연결)
    for i in range(len(costs)):
        if find(parent, costs[i][0]) != find(parent, costs[i][1]):
            union(parent, costs[i][0], costs[i][1])
            answer += costs[i][2]
            cnt += 1
        if cnt == n : break
    
    return answer

    

# 입력
input1 = 4
input2 = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(input1, input2))
