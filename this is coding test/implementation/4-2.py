# 시각
hour = int(input())

count = 0
# 차례대로 시,분,초
for h in range(hour + 1):
    for m in range(60):
        for s in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(h) + str(m) + str(s) :
                count += 1

print(count)
