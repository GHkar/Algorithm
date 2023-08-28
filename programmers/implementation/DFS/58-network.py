# 네트워크
# dfs

def dfs(graph, now, visited):
    visited[now] = True

    # 연결되어 있는 곳은 다 돌기
    for next in graph[now]:
        if visited[next] != True:
            dfs(graph, next, visited)
    
    return True


def solution(n, computers):
    answer = 0
    visited = [False] * n
    graph = [[] for _ in range(n)]

    # 연결된 정보에 따른 그래프 생성
    for computerIndex in range(n):
        for i, v in enumerate(computers[computerIndex]):
            if i != computerIndex and v == 1:
                graph[computerIndex].append(i)

    # dfs로 방문처리
    for i in range(n):
        if visited[i] != True :
            if dfs(graph, i, visited) == True : answer += 1

    return answer


# 입력
input1 = 3
input2= [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(input1, input2))
