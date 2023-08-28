# 타겟 넘버
# dfs

def dfs(numbers, step, total, target):
    if step == len(numbers):
        if total == target : return 1
        else : return 0

    answer = 0
    answer += dfs(numbers, step + 1, total + numbers[step], target)
    answer += dfs(numbers, step + 1, total - numbers[step], target)

    return answer

def solution(numbers, target):
    return dfs(numbers, 0, 0, target)


# 입력
input1 = [1, 1, 1, 1, 1]
input2 = 3

print(solution(input1, input2))
