from collections import deque
first_sequence = deque(input().split(", "))
sekont_sequence = deque(input().split(", "))








palm = 0
willow = 0
crossette = 0

flag = True
for _ in range(len(first_sequence)):
    f_s = int(first_sequence.popleft())
    s_s = int(sekont_sequence.pop())
    if f_s <= 0:
        f_s = int(first_sequence.popleft())

    if s_s <= 0:
        s_s = int(sekont_sequence.pop())

    result = f_s + s_s
    if result % 3 == 0 and result % 5 == 0:
        crossette += 1
        flag = False
    elif result % 3 == 0:
        palm += 1
        flag = False
    elif result % 5 == 0:
        willow += 1
        flag = False
    if flag:
        first_sequence.append(f_s - 1)
        sekont_sequence.append(s_s)
    flag = True
    result = 0

print(palm)
print(willow)
print(crossette)