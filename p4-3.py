def max_num(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = max_num(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max



lst = [3,56,8,38,9,99]
print(max(lst))
