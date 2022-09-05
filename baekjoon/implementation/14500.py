# dfs 정의
def dfs(r, c, idx, total):
    # 결과값 변수
    global ans

    # 현재의 dfs에서 남은 블록이 모두 최댓값에 해당하더라도 현재 ans를 넘기지 못한다면 조기종료
    if ans >= total + max_val * (3 - idx):
        return
    # 4개의 블록을 모두 사용했으면
    if idx == 3:
        # 현재 dfs한 값과 이전까지의 최댓값(ans)을 비교해 더 큰 값을 ans로 반환하고 종료
        ans = max(ans, total)
        return
    # 4개의 블록을 아직 다 사용하지 않았다면
    else :
        # 방향 설정
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 이동하려는 위치가 종이 (배열)안에 있고 방문한 적이 없다면
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                # 만약 2개의 블록을 선택했다면 (ㅗ 모양 블록을 만들어주기 위함)
                if idx == 1:
                    # 방문도장 찍기
                    visit[nr][nc] = 1
                    # 방문도장 찍은 위치에서 dfs 재귀적 호출
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    # 목적지를 풀어주기
                    visit[nr][nc] = 0
                # 방문도장 찍기
                visit[nr][nc] = 1
                # 방문도장 찍은 위치에서 dfs 재귀적 호출
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                # 목적지를 풀어주기
                visit[nr][nc] = 0



# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]

# 좌표 이동거리 행, 열 입력받기
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0

# 종이 중에 가장 큰 값
max_val = max(map(max, arr))

# 종이에 있는 숫자를 하나씩 입력받아
for r in range(N):
    for c in range(M):
        # 방문도장 찍기
        visit[r][c] = 1
        # dfs 호출하여 ans 최댓값 구하기
        dfs(r, c, 0, arr[r][c])
        # 목적지 해제
        visit[r][c] = 0

# 정답 출력
print(ans)
