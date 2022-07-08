# 과제

N = int(input())
work = {}

# 딕셔너리 형태로 만들기
for i in range(N):
    d, w = map(int,input().split())
    if(d in work.keys()) : work[d].append(w)
    else : work[d] = [w]

worklist = sorted(work.items(), reverse=1)

# 최대 과제 마감일을 기준으로 역행
result = 0
points = []

for i in range(worklist[0][0], 0, -1) :
    for w in worklist:
        if w[0] == i:
            points.extend(w[1])
    if len(points) != 0 :
        result = result + max(points)
        points.remove(max(points))

print(result)
