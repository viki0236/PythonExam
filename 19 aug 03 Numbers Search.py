def numbers_searching (*n):

    min_nums = min(n)
    max_nums = max(n)
    required_number = []
    duplicates_nums = []
    for i in range(min_nums, max_nums + 1):
        if i in n:
            dup_num = n.count(i)
            if dup_num > 1:
                duplicates_nums.append(i)
            continue
        else:
            required_number.append(i)
    required_number.append(duplicates_nums)
    return required_number

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))