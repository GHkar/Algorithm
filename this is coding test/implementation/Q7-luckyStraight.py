# 구현 - 럭키 스트레이트

N = list(map(int, input()))
mid = int(len(N) / 2)

if sum(N[:mid]) == sum(N[mid:]) :
    print('LUCKY')
else :
    print('READY')
