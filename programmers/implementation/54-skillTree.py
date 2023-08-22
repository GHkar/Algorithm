# 스킬 트리
# 스킬 트리에 포함되는 스킬이 나오면, now에 넣고 후에 스킬트리 순서와 비교 

from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = deque(skill[:])

        for s in skills:
            if s in skill and s != skill_list.popleft(): break
        else : answer += 1

    return answer


# def check(skill, skill_tree):
#     now = []

#     for s in skill_tree:
#         if s in skill : 
#             now.append(s)

#     for i in range(len(now)):
#         if skill[i] != now[i] : return 0        

#     return 1

# def solution(skill, skill_trees):
#     answer = 0

#     for skill_tree in skill_trees:
#         answer += check(skill, skill_tree)

#     return answer

# 입력
input1 = "CBD"
input2 = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(input1, input2))
