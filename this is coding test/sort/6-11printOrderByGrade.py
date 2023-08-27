# 성적이 낮은 순서로 학생 출력하기

N = int(input())
students = {}

for i in range(N):
    student = input().split( )
    students[student[0]] = int(student[1])

# 학생의 성적으로 정렬 후 이름만 반환하여 배열 생성
# sorted는 무조건 배열로 반환, students를 매개변수 s로 주면 key가 s로 들어가고 반환 값은 value로 지정해줌
students = sorted(students, key = lambda s : students[s])

for s in students:
    print(s, end= ' ')
