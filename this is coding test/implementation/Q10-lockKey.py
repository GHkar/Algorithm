# 구현 - 자물쇠와 열쇠

# 회전 (시계 방향만 구현)
from copy import deepcopy


def rotate(key) :
    rot_key = [[0 for i in range(len(key))] for j in range(len(key))]
    
    for i in range(len(key)):
        column = []
        for j in range(len(key)):
            column.append(key[j][i])

        rot_key[i] = column[::-1]
        # dir = 0 = 시계
        # if dir == 0: 
        # dir = 1 = 반시계
        # else : rot_key[len(key) - i - 1] = column       
    return rot_key

# 이동 (오른쪽, 아래 이동만 구현)
def move(key, dir):
    # dir = 0 = 오른쪽
    if dir == 0:
        for i in range(len(key)):
            for j in range(len(key) - 2, -1, -1):
                val = key[i][j]
                key[i][j] = 1
                key[i][j+1] = val

    # dir = 1 = 아래쪽
    else:
        for i in range(len(key) - 2, -1, -1):
                val = key[i]
                if 1 in val:
                    key[i] = [1 for j in range(len(key))]
                    key[i+1] = val

    return key



def solution(key, lock):
    # 완전 탐색, key를 반전시키고, 회전 및 이동한 것이 lock과 같다면 true, 아니면 false
    for x in range(len(key)) :
        for y in range(len(key)):
            key[x][y] = 1 - key[x][y]
    
    # 진짜 key 회전 3번
    for z in range(3):
        under_key = deepcopy(key)
        # 아래로 이동
        for i in range(len(key)):
            move_key = deepcopy(under_key)
            # 오른쪽 이동
            for j in range(len(key)):
                if move_key == lock :
                    return True
                move_key = move(move_key, 0)
            under_key = move(under_key, 1)
        # 회전
        key = rotate(key)
    
    return False
    

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

if solution(key, lock) : print('true')
else : print('false')
