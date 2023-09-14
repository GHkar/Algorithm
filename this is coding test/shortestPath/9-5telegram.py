# 전보

import heapq

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시
n, m, c = map(int, input().split())

# 최단 거리 리스트
dist = [INF] * (n + 1)

# 연결되어 있는 노드를 표현할 그래프
graph = [[] for _ in range(n + 1)]

# 각 간선에 대한 정보를 입력받기
for _ in range(m):
    # x에서 y로 가는 거리는 z이라고 설정
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        d, now = heapq.heappop(q)

        if dist[now] < d: continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = d + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 수행된 결과를 출력
dijkstra(c)
md = 0
count = -1  # 출발 노드 제외

for d in dist:
    if d != INF:
        count += 1
        md = max(md, d)

print(count, md)

