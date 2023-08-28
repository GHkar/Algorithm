# 단어 변환
# bfs

from collections import deque

def solution(begin, target, words):
    words.insert(0, begin)
    visit = [0] * len(words)
    route = deque()
    route.append(begin)

    while route:
        # 현재 비교하고 싶은 단어
        now = route.popleft()

        if now == target : return visit[words.index(now)]

        for i in range(len(words)):
            if visit[i] == 0:                   # 방문한 적이 없으면 수행
                count = 0
                # 현재 비교 단어의 철자를 하나씩 꺼내서
                for n in range(len(now)):
                    if now[n] == words[i][n]:   # 단어 목록에있는 철자와 일치한다면 카운트를 올림
                        count += 1
                if count == len(now) - 1:       # 현재 단어에서 철자 하나만 바꿔서 만들 수 있는 단어라면 추가해줌
                    route.append(words[i])
                    visit[i] += visit[words.index(now)] + 1

    return 0

# 입력
input1 = "hit"
input2 = "cog"
input3 = ["hot", "dot", "dog", "lot", "log", "cog"]	

print(solution(input1, input2, input3))
