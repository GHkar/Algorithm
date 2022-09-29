from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split(' '))

# 나이트가 이동할 수 있는 6가지 방향 정의
steps = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]

# visted 배열
visited = [[-1] * N for _ in range(N)]

# BFS
def bfs():
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((r1, c1))
    visited[r1][c1] = 0

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        r, c = queue.popleft()
        
        for s in steps:
            next_r = r + s[0]
            next_c = c + s[1]
            # 공간을 벗어나면 무시
            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N:
                continue
            
            # 방문 하지 않은 곳이라면 방문 하기
            if visited[next_r][next_c] == -1:
                visited[next_r][next_c] = visited[r][c] + 1
                queue.append((next_r, next_c))
    # 도착지 값 반환
    return visited[r2][c2]

print(bfs())
