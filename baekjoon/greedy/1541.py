# 잃어버린 괄호

problem = input()

number = problem.split('-')

answer = 0
for num in number :
    if '+' in num :
        answer -= sum(map(int,num.split('+')))
    else:
        answer -= int(num)

answer += (sum(map(int,number[0].split('+'))) * 2)

print(answer)
