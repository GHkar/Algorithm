from collections import deque

# 입력받기
N, K = map(int, input().split(' '))

place = [-1] * 100001

def bfs():
     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append(N)
    place[N] = 0

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        n = queue.popleft()

        for i in range(3):
            if i == 0 :
                next_n = n - 1
            elif i == 1 :
                next_n = n + 1
            else :
                next_n = n * 2

            # 공간을 벗어나면 무시
            if next_n < 0 or next_n > 100000:
                continue
            
            # 방문 하지 않은 곳이라면 방문 하기
            if place[next_n] == -1:
                place[next_n] = place[n] + 1

                queue.append(next_n)
    # 도착지 값 반환
    return place[K]

print(bfs())
