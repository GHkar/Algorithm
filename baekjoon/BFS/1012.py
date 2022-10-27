from collections import deque
T = int(input())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 코드
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    field[x][y] = 2

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4방향에 대해 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M :
                continue
            # 배추가 없는 곳이면 무시
            if field[nx][ny] == 0:
                continue
            # 지렁이가 처음 안착한 배추면 기록
            if field[nx][ny] == 1:
                field[nx][ny] = 2
                queue.append((nx, ny))

# 테스트 케이스만큼 실행
for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]
    cabbages = []
    answer = 0

    # 배추 위치 입력받기
    for _ in range(K):
        X, Y = map(int,input().split())
        field[Y][X] = 1
        cabbages.append([X, Y])

    # 배추가 심어져 있는 곳에서 bfs 돌리기
    for cabbage_y, cabbage_x in cabbages:
        if field[cabbage_x][cabbage_y] == 1:
            answer += 1
            bfs(cabbage_x, cabbage_y)

    print(answer)


