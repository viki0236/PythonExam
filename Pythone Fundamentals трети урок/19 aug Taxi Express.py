from collections import deque

customers_time = deque([el for el in input().split(", ")])
taxi_time = deque([el for el in input().split(", ")])

all_time = 0

flag = True
while flag:

    customers = int(customers_time.popleft())
    if customers <= int(taxi_time.pop()):
        all_time += customers
    else:

        customers_time.appendleft(customers)

    if len(customers_time) <= 0:
        print(f"All customers were driven to their destinations")
        print(f"Total time: {all_time} minutes")
        flag = False
    elif len(taxi_time) <= 0:
        print(f"Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join([str(el) for el in customers_time])}")
        flag = False

