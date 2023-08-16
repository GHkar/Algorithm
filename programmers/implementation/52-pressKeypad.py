# 키패드 누르기

# 거리 계산 함수
def dist(target, pos):
    return abs(target[0] - pos[0]) + abs(target[1] - pos[1])

def solution(numbers, hand):
    pattern = {'L':(1,4,7), 'R':(3,6,9)}
    pos = {'L':[0,3], 'R':[2,3]}
    result = []

    # 키패드 눌렀을 때
    def press(which, coord):
        result.append(which)
        pos[which] = coord

    for number in numbers:
        # 왼쪽을 고정
        choose = 'L'
        target = [0, (number - 1) // 3]

        if number in pattern['L']: pass
        elif number in pattern['R']: choose = 'R'
        else:   # 2, 5, 8, 0 일 때
            target = [1, 3 if number == 0 else (number - 1) //3]
            left, right = dist(target, pos['L']), dist(target, pos['R'])

            if right < left : choose = 'R'
            elif right == left and hand =='right': choose = 'R'

        press(choose, target)
    
    return ''.join(result)

# 입력
input1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
input2 = "right"

print(solution(input1, input2))
