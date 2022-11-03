def sum(lst):
    if lst == []:
        return 0
    return lst[0]+ sum(lst[1:])


lst = [2,4,6,8,10]
print(sum(lst))