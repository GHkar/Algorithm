# 괄호 변환
# dfs

# 올바른 괄호인지 확인
def check(str):
    stack = []

    for s in str:
        if s == '(' : stack.append('(')
        elif stack: stack.pop()
        else : return False
    return True


def dfs(p):
    # 입력이 빈 문자열이면 빈 문자열을 반환
    if not p : return p

    balance = 0

    # 문자열을 균형잡힌 괄호 문자열 u, v로 분리
    for i in range(len(p)):
        if p[i] == '(': balance +=1
        else : balance -=1

        # 최소 균형잡힌 괄호를 찾아냈다면, 그 다음부터 진행
        if balance == 0 :
            # 나눠진 u가 올바른 괄호라면 나머지 v에 대해서 다시 재귀 
            if check(p[:i+1]) : 
                return ''.join([p[:i+1], *dfs(p[i+1:])])
            else :
                new = ['(', *dfs(p[i+1:]), ')']
                for u in p[1:i]:
                    if u == '(' : new.append(')')
                    else : new.append('(')

                return ''.join(new)
            

def solution(p):
    return dfs(p)


# 입력
input1 = "()))((()"

print(solution(input1))
