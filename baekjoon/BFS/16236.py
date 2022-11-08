# 아기상어
from collections import deque
from unittest import result
N = int(input())


# 전체 장소 받기
sea = []
for _ in range(N):
    sea.append(list(map(int, input().split())))


now = [0, 0]

# 아기 상어 위치
for x in range(N):
    for y in range(N):
        if sea[x][y] == 9 :
            now = [x, y]
            sea[x][y] = 0

# 이동
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 아기 상어 몸무게
baby_shark = 2
# 몸무게 증가를 위한 카운트
count = 0
# 걸린 시간
answer = 0

# BFS
def bfs():
    global answer
    global now
    global count
    global baby_shark
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((now[0], now[1]))
    
    dist = [[-1] * N for _ in range(N)]
    dist[now[0]][now[1]] = 0
    eat = []

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        x, y = queue.popleft()
        
        for step in range(4):
            next_x = x + dx[step]
            next_y = y + dy[step]

            # 공간을 벗어나면 무시
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue

            # 상어보다 작거나 같은 크기의 물고기 일때 + 방문하지 않은 곳만 이동
            if sea[next_x][next_y] <= baby_shark and dist[next_x][next_y] == -1 :
                # 물고기 먹기
                if sea[next_x][next_y] < baby_shark and sea[next_x][next_y] != 0 :
                    eat.append([next_x, next_y, dist[x][y]+1])
                # 먹지않고 이동
                else:
                    dist[next_x][next_y] = dist[x][y] + 1
                    queue.append((next_x, next_y))

    # 먹을 물고기가 있다면
    if eat :
        # 거리가 짧은 순으로 먼저 정렬 후 위에 있는 물고기, 왼쪽 물고기부터 잡아먹기 
        eat.sort(key=lambda x: (x[2], x[0], x[1]))
        answer += eat[0][2]
        now = [eat[0][0], eat[0][1]]
        sea[eat[0][0]][eat[0][1]] = 0
        
        # 아기 상어 몸무게 올리기
        count += 1
        if baby_shark == count :
            count = 0
            baby_shark += 1

        return 0
    else :
        return -1

# 엄마 상어 부르기 전까지 계속 돌리기
while(True):
    result = bfs()
    if result == -1 :
        break

print(answer)
