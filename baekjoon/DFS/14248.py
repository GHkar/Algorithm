# 돌다리의 돌 개수
n = int(input())

# 돌 거리
stone = [0] + list(map(int, input().split()))

# 시작점
start = int(input())

# 돌 방문 여부
visit = [False] * (n + 1)

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x):
    global result
    # 현재 노드를 아직 방문하지 않았다면
    if visit[x] == False:
        visit[x] = True
        # 왼쪽 오른쪽 차례대로 호출
        left = x - stone[x]
        right = x + stone[x]
        if left > 0:
            dfs(left)
        if right < n+1:
            dfs(right)


# 시작점에서 시작
dfs(start)

print(visit.count(True))   # 정답 출력
