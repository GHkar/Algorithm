# 떡볶이 떡 만들기

import sys

N, M = map(int, input().split())
rice = list(map(int, sys.stdin.readline().rstrip().split( )))


def binary_search(rice, target, start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        result = 0
        # 떡을 자른 나머지를 더했을 때의 결과 계산
        for r in rice :
            rest = r - mid
            if  rest > 0 : result += rest
        # 찾은 경우 값 반환
        if result == target :
            answer = mid
            break
        # 결과 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        elif result > target :
            start = mid + 1
            answer = mid
        # 결과 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        else : end = mid - 1

    return answer


# 이진 탐색 수행 결과 출력
print(binary_search(rice, M, 0, max(rice)))

