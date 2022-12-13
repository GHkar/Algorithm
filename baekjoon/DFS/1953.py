# 학생들의 수
N = int(input())

# 싫어하는 학생의 정보
students = []
for i in range(N):
    line = list(map(int, input().split()))
    students.append(line[1:])


# 학생 방문 여부
visit = [False] * N

# 팀
team = [[],[]]

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, now):
    global team

    # 현재 노드를 아직 방문하지 않았다면
    if visit[x] == False:
        visit[x] = True
        team[now].append(x+1)

        # 싫어하는 학생은 반대편에 넣기
        for s in students[x] :
            dfs(s-1, not(now))
        


# 방문하지 않은 경우, 먼저 청팀으로 배정 받으나 청팀에 싫어하는 사람이 있을 경우 백팀으로 시작
for x in range(N):
    now = False
    if visit[x] == False :
        for i in students[x] :
            if  i in team[False] : 
                now = not(now)
                break
    dfs(x, now)

# 다른 팀에 아무도 없을 경우
for i in range(2):
    if len(team[i]) == 0 :
        team[i].append(team[not(i)][0])
        team[not(i)] = team[not(i)][1:]

# 정답 출력
for i in range(2):
    team[i].sort()
    print(len(team[i]))
    for i in team[i]:
        print(i, end=" ")
    print()
