# https://www.acmicpc.net/problem/5635

import sys

students_dict = {}
for _ in range(int(sys.stdin.readline())):
    # student = ["mickey", "1", "10", "1991"]
    student = list(sys.stdin.readline().split())
    students_dict[student[0]] = int(student[3] + student[2] + student[1])
print(students_dict)
students_dict = sorted(students_dict.items(), key=lambda item: item[1])
print(students_dict)
