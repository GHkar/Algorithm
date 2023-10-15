# 정렬 - 국영수
from collections import defaultdict

N = int(input())
# 이름, 국어, 영어, 수학 점수 순으로 제공
grade = defaultdict(list)

for n in range(N):
    student = list(input().split())
    grade[student[0]] = list(map(int, student[1:]))

# 국어 감소, 영어 증가, 수학 감소, 이름 사전순 증가
sorted_grade = sorted(grade.items(), key = lambda item: (-item[1][0], item[1][1], -item[1][2], item[0]))


for name in sorted_grade:
    print(name[0])
