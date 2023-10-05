# DFS/BFS - 특정 거리의 도시 찾기
from collections import defaultdict
from collections import deque

# 도시 개수, 도로 개수, 거리 정보, 출발 도시
N, M, K, X = map(int,input().split())

# 그래프 생성
node = defaultdict(list)

for m in range(M):
    start, end = map(int, input().split())
    node[start].append(end)

# 방문, 거리
visited = [0] * (N + 1)

que = deque()
que.append(X)

while que:
    now = que.popleft()

    # 방문한 적 없을 시 최단 거리 갱신
    for n in node[now]:
        if visited[n] == 0 :
            visited[n] = visited[now] + 1
            que.append(n)

# 도달 못하면 -1 출력, 아니면 오름차순으로 출력
if K not in visited:
    print(-1)
else:
    for i in range(1, N+1):
        if visited[i] == K:
            print(i)

