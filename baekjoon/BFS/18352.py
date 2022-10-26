from collections import deque

# 입력받기
N, M, K, X = map(int, input().split(' '))

road = [[] for _ in range(N+1)]


for i in range(M):
    n, m = map(int, input().split(' '))
    road[n].append(m)

# BFS 메서드 정의
def bfs(road, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = 0
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        now_node = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for next_node in road[now_node]:
            if visited[next_node] == -1:
                queue.append(next_node)
                visited[next_node] = visited[now_node] + 1


# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [-1] * (N + 1)

# 정의된 BFS 함수 호출
bfs(road, X, visited)

# 최단 거리가 정확히 K인 모든 도시들의 번호를 출력
if K not in visited : print(-1)
else :
    number = 0
    for v in visited :
        if v == K :
            print(number)
        number += 1
