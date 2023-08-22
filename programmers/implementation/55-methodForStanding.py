# 줄 서는 방법
# 순열, 앞 숫자 하나를 선택하면 나머지 남은 숫자의 조합이 팩토리얼만큼 남음

def fact(n):
    if(n > 1): return n * fact(n-1)
    else: return 1

def solution(n, k):
    answer = []
    numbers = list(range(1, n+1))

    while numbers:
        # 숫자 선택 시 남은 수 하나 당 조합할 수 있는 방법의 개수, 팩토리얼
        turn = fact(len(numbers) - 1)
        for i in range(0, len(numbers)):
            if k <= turn * (i + 1) :            # 그 조합 방법 안에 k가 들어가면
                answer.append(numbers.pop(i))   # 숫자 선택 후 
                k -= turn * i                   # 남은만큼 제외해줌
                break

    return answer


# from math import factorial

# def solution(n, k):
#     numbers = list(range(1, n+1))
#     answer = []
#     k -= 1

#     while numbers:
#         idx, k = divmod(k, factorial(len(numbers) - 1))
#         answer.append(numbers.pop(idx))

#     return answer



# 입력
input1 = 4
input2 = 5

print(solution(input1, input2))
