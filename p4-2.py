def l_list(lst):
    if len(lst) == 0:
        return 0
    return 1+ l_list(lst[1:])


lst = [1,2,3,8]
print(l_list(lst))