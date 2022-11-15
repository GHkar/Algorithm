# 컴퓨터의 수
n = int(input())

# 컴퓨터 쌍의 수
m = int(input())


# 연결된 네트워크 입력
network = []
for i in range(m):
    nt = list(map(int, input().split()))
    network.append(nt)

    # 양방향 구현
    nt = [nt[1], nt[0]]
    network.append(nt)

# 컴퓨터 순서대로 정렬
network.sort(key=lambda x: x[0])

# 컴퓨터 방문 여부
computer = [False] * (n + 1)

result = -1

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x):
    global result
    # 현재 노드를 아직 방문하지 않았다면
    if computer[x] == False:
        # 해당 노드를 방문 처리
        result += 1
        computer[x] = True
        # 연결된 컴퓨터 차례대로 호출
        for c in network:
            if c[0] == x:
                dfs(c[1])
            
            if c[0] > x:
                break

# 1번 컴퓨터로 웜 뿌리기
dfs(1)

print(result)   # 정답 출력
