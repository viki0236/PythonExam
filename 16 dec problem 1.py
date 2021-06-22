from collections import deque

males = [int(el) for el in input().split()]
females = [int(el) for el in input().split()]

males = deque(males)
females = deque(females)

counter = 0

while True:
    if len(males) == 0:
        break
    if len(females) == 0:
        break
    ma = males.pop()
    fe = females.popleft()
    if ma <= 0:
        ma = males.pop()
    if fe <= 0:
        fe = females.popleft()
    if ma == fe:
        counter += 1
        continue
    else:
        males.appendleft(ma - 2)

print(f"Matches: {counter}")
if len(males) > 0:

    print(f"Males left: {[i for i in males]}")
else:
    print("males left: none")
if len(females) > 0:

        print(f"Females left: {females}")
else:
    print("Females left: none")