from collections import deque

def list_manipulator (l, comand, were, *n):
    ll = deque(l)

    if comand == "add":
        if were == "end":
            ll.append(n)
        elif were == "beginning":
            ll.appendleft(n)
    elif comand == "remove":
        if were == "end":
            if n:
                for i in range(n):
                    ll.pop()
            else:
                ll.pop()
        elif were == "beginning":
            if n:
                for i in range(n):
                    ll.popleft()
            else:
                ll.popleft()



    return ll

print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
