# 부품 찾기

import sys

N = int(input())
have = list(map(int, input().split()))
have.sort()
M = int(input())
find = list(map(int, sys.stdin.readline().rstrip().split( )))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target : return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target : end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else : start = mid + 1

    return None


# 이진 탐색 수행 결과 출력
for f in find :
    result = binary_search(have, f, 0, N - 1)
    if result == None : print("no", end= ' ')
    else : print("yes", end= ' ')
