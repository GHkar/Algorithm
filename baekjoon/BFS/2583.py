from collections import deque

# 입력받기
M, N, K = map(int, input().split(' '))

paper = [[False] * N for _ in range(M)]

for i in range(K):
    nemo = list(map(int, input().split(' ')))

    for y in range(nemo[0], nemo[2], 1):
        for x in range(nemo[1], nemo[3], 1):
            paper[x][y] = True


move_x = [0, 0, 1, -1]
move_y = [1, -1, 0, 0]

def bfs(x, y):
     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    paper[x][y] = True

    area = 1
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        r, c = queue.popleft()

        for i in range(4):
            next_r = r + move_x[i]
            next_c = c + move_y[i]
            # 공간을 벗어나면 무시
            if next_r < 0 or next_r >= M or next_c < 0 or next_c >= N:
                continue
            
            # 방문 하지 않은 곳이라면 방문 하기
            if paper[next_r][next_c] == False:
                paper[next_r][next_c] = True
                area += 1
                queue.append((next_r, next_c))
    # 도착지 값 반환
    return area

answer = []

for x in range(M):
    for y in range(N):
        if paper[x][y] == False:
            answer.append(bfs(x, y))


print(len(answer))
answer.sort()
for a in answer :
    print(a, end = ' ')
