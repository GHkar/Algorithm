# 그리디 - 문자열 뒤집기

S = list(map(int,input()))

zero = 0
one = 0

def zeroOrOne(v):
    global zero, one
    if v == 0 :
        zero += 1
    else :
        one += 1

now = S[0]
zeroOrOne(now)

for s in S:
    if now != s :
        now = s
        zeroOrOne(s)

print(min(zero, one))
