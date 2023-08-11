#  디스크 컨트롤러 - 힙 트리

from heapq import heappush as push, heappop as pop

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 모든 작업을 가장 짧은 순서대로 넣기
        for job in jobs:
            if start < job[0] <= now:
                push(heap, job[::-1])

        # 시간 합 및 처리
        if len(heap) > 0:
            cur = pop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        else :
            now += 1

    return answer // len(jobs)

input = [[0,3],[1,9],[2,6]]
print(solution(input))
