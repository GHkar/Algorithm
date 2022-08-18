# 효율적인 화폐 구성

# 정수 N, M을 입력받기
n, m = map(int, input().split())

# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))


# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [10001] * ( m + 1 )

# 다이나믹 프로그래밍 진행
dp[0] = 0
for i in range(n):
    for j in range(array[i], m + 1) :
        if dp[j - array[i]] != 10001 : #(j-array[i])원을 만들 방법이 있는 경우
            dp[j] = min(dp[j], dp[j - array[i]] + 1)

# 계산된 결과 출력
print(dp[m])
