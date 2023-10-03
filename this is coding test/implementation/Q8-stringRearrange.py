# 구현 - 문자열 재정렬
S = input()
# A-Z의 ord 유니코드 정수 65 - 89
# 0-9의 ord 유니코드 정수 48 - 57
# isalpha()라는 함수 존재

sum = 0
answer = []
for s in S :
    if ord(s) in range(48, 58) :
        sum += int(s)
    else :
        answer.append(s)
answer.sort()
if sum != 0 : answer.append(str(sum))

print(''.join(answer))
