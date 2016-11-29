def bubble_sort(lst):
    new_list = lst[:]
    is_sorted = False
    while is_sorted == False:
        idx = 0
        nswaps = 0

        lstRange = 0
        if len(new_list) % 2 == 0:
            lstRange = len(new_list)
        else:
            lstRange = len(new_list) - 1

        while idx < lstRange:
            a = new_list[idx]
            b = new_list[idx+1]
            if a > b:
                new_list[idx] = b
                new_list[idx+1] = a
                nswaps += 1
            idx = idx + 1

        if nswaps == 0:
            is_sorted = True

    return new_list
