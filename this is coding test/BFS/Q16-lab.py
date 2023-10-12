# DFS/BFS - 연구소

from collections import deque
from copy import deepcopy


# 세로, 가로
N, M = map(int, input().split())
research = []
for n in range(N):
    research.append(list(map(int, input().split())))

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(start, research):
    que = deque()
    que.append(start)

    while que:
        now_x, now_y = que.popleft()

        # 4 방향으로 모두 가보기
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            
            # 지도를 벗어나면
            if next_x < 0 or next_y < 0 or next_x >= M or next_y >= N:
                continue
            # 벽이 아니면 바이러스 퍼뜨리기
            elif research[next_y][next_x] == 0 :
                research[next_y][next_x] = research[now_y][now_x]
                que.append([next_x, next_y])

    return research


answer = 0
# 벽 세워보기
def dfs(count):
    global answer
    # 울타리가 3개 설치된 경우
    if count == 3:
        temp = deepcopy(research)
        for y in range(N):
            for x in range(M):
                if research[y][x] == 2:
                    start = [x, y]
                    temp = bfs(start, temp)

        result = 0
        for t in temp:
            result += t.count(0)
        answer = max(answer, result)
        return

    # 빈 공간에 울타리 설치
    for i in range(N):
        for j in range(M):
            if research[i][j] == 0:
                research[i][j] = 1
                count += 1
                dfs(count)
                research[i][j] = 0
                count -= 1

dfs(0)
print(answer)


