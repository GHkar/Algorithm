import sys
sys.setrecursionlimit(10**6)

# 구구 방의 수
N = int(input())

# 집 구조, 방 정보 입력
guguHome = [[] for i in range(N + 1)]


for i in range(N-1):
    start, end, dist = list(map(int, input().split()))
    guguHome[start].append([end, dist])
    # 양방향 구현
    guguHome[end].append([start, dist])

# 방 거리
dist = [0] * (N + 1)

# 방 방문 여부
visited = [False] * (N + 1)


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, now_dist):
    visited[x] = True
    # 해당 노드에 이동 거리 넣기
    dist[x] = now_dist

    # 연결된 방 차례대로 호출
    for r in guguHome[x]:
        # 이동할 방을 아직 방문하지 않았다면
        if visited[r[0]] == False:
            dfs(r[0], dist[x] + r[1])



# 입구에서 출발하기
dfs(1, 0)

print(max(dist))   # 정답 출력
