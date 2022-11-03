def quickSort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greader = [i for i in lst[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greader)


lst = [3,566,78,44,66,2,3,98]
print(quickSort(lst))