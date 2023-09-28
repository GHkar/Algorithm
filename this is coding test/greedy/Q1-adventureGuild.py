# 그리디 - 모험가 길드

N = int(input())
fear = list(map(int, input().split()))

fear.sort()     # 공포를 오름차순으로 정렬
result = 0      # 총 그룹의 수
number = 0      # 그룹 안에 들어간 사람

for f in fear :
    number += 1         # 그룹에 한명씩 넣기
    if number >= f :    # 현재 그룹 안에 들어온 사람 수가 공포 수치보다 같거나 높다면 그룹 결성
        result += 1     # 총 그룹 수 증가
        number = 0      # 초기화

print(result)
