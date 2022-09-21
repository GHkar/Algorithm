# 가로, 세로, 회전
N, M, R = map(int, input().split( ))

array = []
for i in range(N):
    array.append(list(map(int, input().split( ))))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 원의 개수
circleNum = min(N,M)
n_array = [item[:] for item in array]
# 다음으로 넘어가는 변수
nextnum = 0
# 이동 횟수
for r in range(R):
    # down, right, up, left
    directionStartPoint = [[0,0], [N-1,1], [N-2,M-1], [0,M-2]]
    # 한 원을 이동
    for n in range(int(circleNum/2)):
        # 4 방향으로 이동
        for direction in range(4):
            # down, up
            if direction%2 == 0:
                x = directionStartPoint[direction][0]
                y = directionStartPoint[direction][1]
                n_array[x][y] = nextnum
                # down
                if direction == 0:
                    for j in range(N-(2*n)):
                        nx = x + dx[direction]
                        ny = y + dy[direction]
                        if j == (N-(2*n)) - 1 : nextnum = array[x][y]
                        else: n_array[nx][ny] = array[x][y]
                        x = nx
                        y = ny
                    directionStartPoint[direction][0] += 1
                    directionStartPoint[direction][1] += 1
                else :  # up
                    for j in range(N-(2*n)-1):
                        nx = x + dx[direction]
                        ny = y + dy[direction]
                        if j == (N-(2*n)) - 2 : nextnum = array[x][y]
                        else: n_array[nx][ny] = array[x][y]
                        x = nx
                        y = ny
                    directionStartPoint[direction][0] -= 1
                    directionStartPoint[direction][1] -= 1
            # right, left
            else:
                x = directionStartPoint[direction][0]
                y = directionStartPoint[direction][1]
                n_array[x][y] = nextnum
                for j in range(M-(2*n)-1):
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    if j == (M-(2*n)) - 2 : nextnum = array[x][y]
                    else: n_array[nx][ny] = array[x][y]
                    x = nx
                    y = ny
                # 시작 지점 다음으로 넘겨주기
                if direction == 1:
                    directionStartPoint[direction][0] -= 1
                    directionStartPoint[direction][1] += 1
                else :
                    directionStartPoint[direction][0] += 1
                    directionStartPoint[direction][1] -= 1


        # 마지막에 다시 맨 처음 값 넣어주기
        if n == 0 and circleNum != 2:
            n_array[directionStartPoint[0][0]][directionStartPoint[0][1]] = nextnum

    # 바뀐 원을 다시 대입
    array = [item[:] for item in n_array]

for arr in n_array :
    for a in arr:
        print(a, end= ' ')
    print()
    
    
