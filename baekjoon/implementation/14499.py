# N,M을 공백으로 구분하여 입력받기
n, m, x, y, k = map(int, input().split())


# 전체 지도 정보를 입력받기
dice_map = []
for i in range(n):
    dice_map.append(list(map(int, input().split())))

# 명령 입력받기
command = list(map(int, input().split()))

# 주사위 만들기
dice = [0, 0, 0, 0, 0, 0, 0]

# 동,서,북,남 방향 정의
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 주사위 순서 변경
def change_dice(c):
    global dice
    n_dice = dice[:]
    if c == 1 :
        n_dice[1] = dice[4]
        n_dice[3] = dice[1]
        n_dice[4] = dice[6]
        n_dice[6] = dice[3]
    elif c == 2:
        n_dice[1] = dice[3]
        n_dice[3] = dice[6]
        n_dice[4] = dice[1]
        n_dice[6] = dice[4]
    elif c == 3:
        n_dice[1] = dice[5]
        n_dice[2] = dice[1]
        n_dice[5] = dice[6]
        n_dice[6] = dice[2]
    elif c == 4:
        n_dice[1] = dice[2]
        n_dice[2] = dice[6]
        n_dice[5] = dice[1]
        n_dice[6] = dice[5]
    dice = n_dice[:]

# 명령 실행
for c in command:
    nx = x + dx[c]
    ny = y + dy[c]
    
    # 이동하기
    if nx < n and nx > -1 and ny < m and ny > -1:
        x = nx
        y = ny
        # 이동에 맞춰 주사위 굴리기
        change_dice(c)
        # 바닥에 있는 값이 0 이면 주사위 바닥의 값이 복사
        if dice_map[x][y] == 0:
            dice_map[x][y] = dice[6]
        else:
            dice[6] = dice_map[x][y]
            dice_map[x][y] = 0

        print(dice[1])
