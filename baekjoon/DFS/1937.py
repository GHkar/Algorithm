import sys
sys.setrecursionlimit(10**6)


# 대나무 숲 크기
N = int(input())

# 대나무 정보
bamboo = []
for i in range(N):
    line = list(map(int, input().split()))
    bamboo.append(line)


# 이동
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 판다 최대 이동 횟수
visit = [[0] * N for _ in range(N)]

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    global visit
    # 현재 노드를 아직 방문하지 않았다면
    if visit[x][y] == 0:

        visit[x][y] = 1

        for step in range(4):
            next_x = x + dx[step]
            next_y = y + dy[step]

            # 공간을 벗어나면 무시
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue
            
            # 다음 대나무가 현재 판다가 먹은 대나무보다 크면 이동
            if bamboo[x][y] < bamboo[next_x][next_y]:
                # 이미 기록이 되어 있고, 그 값이 현재값보다 크면 해당 값을 가져옴
                if visit[next_x][next_y] != 0:
                    if visit[x][y] <= visit[next_x][next_y]:
                        visit[x][y] = visit[next_x][next_y] + 1
                else:
                    visit[x][y] = max(visit[x][y], 1 + dfs(next_x, next_y))

    return visit[x][y]


# 차례대로 시작하기, 단 이미 방문하지 않은 곳만
for x in range(N):
    for y in range(N):
        if visit[x][y] == 0:
            dfs(x, y)

print(max(map(max,visit)))
