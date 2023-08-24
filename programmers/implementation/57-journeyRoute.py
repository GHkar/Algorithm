# 여행 경로
# dfs
from collections import defaultdict

answer = []

def dfs(graph, now, route, max_num):
    if max_num == len(route):
        answer.append(route)

    for i, destination in enumerate(graph[now]):    
        graph[now].pop(i)
        # * route는 route의 요소를 unpacking하는 것으로 만약 route 안에 [a,b,c]가 있다면 각 요소를 하나의 객체로 꺼내줌
        dfs(graph, destination, [*route, destination], max_num)
        graph[now].insert(i, destination)


def solution(tickets):
    # 그래프 만들기, defaultdict는 해당값이 비어있을 경우 자동으로 빈리스트로 생성해줌
    graph = defaultdict(list)

    for a, b in tickets: graph[a].append(b)
    for key in graph.keys() : graph[key].sort()
    
    dfs(graph,"ICN", ["ICN"], len(tickets)+1)

    return answer[0]



# 입력
input1 =  [["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]

print(solution(input1))
