# 뒤집기

S = list(map(int,input()))


zero = 0
one = 0

def oneorzero (v) :
    global zero, one
    if v == 1 : one = one + 1
    else : zero = zero + 1


now = S[0]
oneorzero(now)

for s in S :
    if s != now :
        now = s
        oneorzero(now)

print(min(zero,one))
     
