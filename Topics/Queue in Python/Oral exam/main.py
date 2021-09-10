from collections import deque

exams = deque()
num_records = int(input())

for _ in range(num_records):
    action = input()
    if action.startswith("READY"):
        student = action.split(" ")[-1]
        exams.appendleft(student)
    elif action == "EXTRA":
        student = exams.pop()
        exams.appendleft(student)
    elif action == "PASSED":
        print(exams.pop())
