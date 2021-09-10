from collections import deque

my_queue = deque()
operations = int(input())

for _ in range(operations):
    action = input()
    if action.startswith("ENQUEUE"):
        num = action.split(" ")[-1]
        my_queue.append(num)
    elif action.startswith("DEQUEUE"):
        my_queue.popleft()


for number in my_queue:
    print(number)
