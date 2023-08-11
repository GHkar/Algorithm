# 보석 쇼핑 - 투 포인터

def solution(gems):
    # 1. 보석의 종류와 현재 가지고 있는 보석을 정의
    kind = len(set(gems))
    size = len(gems)
    answer = [0, size -1]   # 정답 초깃값은 범위를 최대로 설정

    dic = {gems[0] : 1}     # 장바구니에 첫 물건 넣어놓기
    start = end = 0         # 투 포인터

    # 2. 시작 포인터부터 끝 포인터까지 전부 구매한다고 했을 때 모든 종류의 보석을 살 수 있는지 확인
    while end < size:
        if len(dic) < kind: # 보석을 모두 포함 못한다면
            end += 1
            if end == size: break
            dic[gems[end]] = dic.get(gems[end], 0) + 1  # 보석 추가
        else:
            if(end - start + 1) < (answer[1] - answer[0] + 1): answer = [start, end]    # 범위가 현재 답보다 더 작다면 정답 바꾸기
            if dic[gems[start]] == 1: del dic[gems[start]]  # 시작 범위를 옆으로 옮기면서 장바구니에 담아뒀던 보석 빼기
            else: dic[gems[start]] -= 1
            start += 1

    # 3. 구간을 보정하고 정답을 반환
    answer[0] += 1
    answer[1] += 1

    return answer

# 입력
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

print(solution(gems))
