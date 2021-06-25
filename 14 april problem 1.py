from collections import deque

piza = input().split(", ")
piza = deque(piza)
rabotnici = input().split(", ")
total_count = 0
while not len(piza) <= 0 and not len(rabotnici) <= 0:
    piz = int(piza.popleft())

    if piz <= 10:
        if piz > 0:
            total_count += piz
            rabot = int(rabotnici.pop())
            if rabot > 0:
                for _ in range(len(piza) or len(rabotnici)):
                    piz = piz - rabot
                    if piz > 0:
                        if rabotnici:
                            rabot = int(rabotnici.pop())
                        else:
                            piza.appendleft(piz)
                    else:

                        break

if len(piza) > 0:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in piza])}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_count}")
    print(f"Employees: {', '.join(rabotnici)}")