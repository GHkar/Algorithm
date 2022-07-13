# 불 끄기

result = []


bulb = [[-1 for i in range(12)]]
move = [[0,0], [-1, 0], [1,0], [0,-1], [0,1]] # 중간, 위, 아래, 왼쪽, 오른쪽


for i in range(10) :
    bulb.append([-1] + list(input()) + [-1])

bulb.append([-1 for i in range(12)])


# 1 << 10 = 1024
for case in range(1024) :
    
    press = 0
    # 얕은 복사
    tmp_bulb = [bulb[i][:] for i in range(12)]

    # 총 1024개의 케이스에 대해 맨 윗 줄의 불 누르기
    mask = 1
    for j in range(10,0,-1):
        if case & mask:
            for m in move :
                if tmp_bulb[1+m[0]][j+m[1]] == '#' : tmp_bulb[1+m[0]][j+m[1]] = 'O'
                elif tmp_bulb[1+m[0]][j+m[1]] == 'O' : tmp_bulb[1+m[0]][j+m[1]] = '#'
            press += 1
        mask <<= 1
    # 케이스에 대해서 2열 부터 윗 불이 켜진 경우에만 불 누르게 하기
    for i in range(2, 11, 1) :
        for j in range(1, 11, 1) :
            if tmp_bulb[i-1][j] == 'O':
                for m in move :
                    if tmp_bulb[i+m[0]][j+m[1]] == '#' : tmp_bulb[i+m[0]][j+m[1]] = 'O'
                    elif tmp_bulb[i+m[0]][j+m[1]] == 'O' : tmp_bulb[i+m[0]][j+m[1]] = '#'
                press += 1

    if 'O' not in tmp_bulb[10] : result.append(press)


if len(result) != 0 : print(min(result))
else : print(-1)



# print("bulb")

# for i in range(1, 11, 1) :
#     for j in range(1, 11, 1) :
#         print(bulb[i][j], end="")
#         if j == 10: print("")



"""
O#O#######
##O#######
O#########
O#########
##########
##########
##########
##########
##########
##########
"""
