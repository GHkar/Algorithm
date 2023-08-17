# 2개 이하로 다른 비트
# 짝수 -> 오른쪽 한개, 즉 +1
# 홀수 -> 0이 나오고 오른쪽 비트랑 같이 10 으로 바꿔줌, 나머지는 그대로

# def solution(numbers):
#     answer = []
#     for number in numbers:
#         if number % 2 == 0 : answer.append(number + 1)
#         else :
#             number = f'0{bin(number)[2::]}'
#             number = f"{number[:number.rindex('0')]}10{number[number.rindex('0') + 2:]}"
#             answer.append(int(number, 2))

#     return answer

def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0 : answer.append(number + 1)
        else :
            change = f'0{bin(number)[2::]}'
            i = change.rindex('0')
            lc = list(change)
            lc[i], lc[i+1] = '1', '0'
            answer.append(int(''.join(lc), 2))

    return answer

# 입력
input1 = [2,7]

print(solution(input1))
