# 방바닥 크기
N, M = map(int, input().split())

# 방 바닥 디자인
floor = []
for i in range(N):
    line = input()
    floor.append(line)


# 방바닥 방문 여부
visit = [[False] * M for _ in range(N)]

result = 0
# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    global result
    # 현재 노드를 아직 방문하지 않았다면
    if visit[x][y] == False:
        visit[x][y] = True
        # 가로인지 세로인지 판단 후 DFS 호출
        if floor[x][y] == '-' and (y + 1) < M :
            if floor[x][y+1] != '-' : result += 1
            dfs(x, y + 1)
        elif floor[x][y] == '|' and (x + 1) < N :
            if floor[x+1][y] != '|' : result += 1
            else : dfs(x + 1, y)
        else : result += 1
    if False in visit[x] and (y + 1) < M : dfs(x, y + 1)


# 각 가로마다 시작
for x in range(N):
    if False in visit[x] : dfs(x, 0)

print(result)   # 정답 출력
