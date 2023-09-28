# 그리디 - 곱하기 혹은 더하기

S = input()

result = int(S[0])
for s in S[1:]:
    s = int(s)
    if result <= 1 or s <= 1:
        result += s
    else :
        result *= s


print(result)
