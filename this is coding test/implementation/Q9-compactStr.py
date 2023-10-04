# 구현 - 문자열 압축
def solution(s):
    answer = len(s)
    now = 1     # 비교할 개수
    
    while now != len(s):
        start = 0
        end = start + now
        count = 1
        compact = ''
        while True:
            # break
            if end + now > len(s) :
                if count != 1:
                    compact += str(count)
                compact += s[start:]
                break
            # 앞이랑 뒤가 같다면
            if s[start:end] == s[start+now:end+now] :
                count += 1
            # 다르다면
            else :
                if count != 1:
                    compact += str(count)
                compact += s[start:end]
                count = 1

            start += now
            end += now
        # 최솟값 찾기
        answer = min(answer, len(compact))
        now += 1
    return answer

print(solution('xababcdcdababcdcd'))

