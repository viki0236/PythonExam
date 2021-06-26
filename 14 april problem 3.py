def flights (*flig):
    dic = {}

    for i in range(0, len(flig), 2):
        if flig[i] != "Finish":
            if flig[i] not in dic:
                dic[flig[i]] = flig[i + 1]
            else:
                dic[flig[i]] += flig[i + 1]
        else:
            break

    return dic

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))