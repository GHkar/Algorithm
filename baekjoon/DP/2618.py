import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
W = int(input())

case = [(1,1),(N,N)] # 첫번째, 두번째 경찰차 위치
for i in range(W):
    case.append(tuple(map(int,input().split())))

# dp 배열 초기화
dp = [[-1 for col in range(W+2)] for row in range(W+2)]

def make_dp (x,y):
    if x > W or y > W : return 0
    if dp[x][y] != -1 : return dp[x][y]

    next = max(x,y) + 1

    # 1번 차가 다음 사건으로 움직였을 때
    X = make_dp(next, y) + abs(case[next][0]-case[x][0]) + abs(case[next][1]-case[x][1])
    # 2번 차가 다음 사건으로 움직였을 때
    Y = make_dp(x, next) + abs(case[next][0]-case[y][0]) + abs(case[next][1]-case[y][1])

    dp[x][y] = min(X, Y)

    return dp[x][y]


def navi(x,y):
    if x > W or y > W: return
    next = max(x,y) + 1
    X = abs(case[next][0]-case[x][0]) + abs(case[next][1]-case[x][1])
    Y = abs(case[next][0]-case[y][0]) + abs(case[next][1]-case[y][1])

    if dp[next][y]+X < dp[x][next]+Y:
        print(1)
        navi(next,y)
    else:
        print(2)
        navi(x,next)
    return

print(make_dp(0, 1))
navi(0,1)
