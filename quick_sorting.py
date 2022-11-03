def findSmallest(my_list):
    smallest = my_list[0]
    smallest_index = 0

    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
            smallest_index = i
            # print(smallest)
    return smallest_index

def quickSorting(my_list):
    new_list = []
    for i in range(len(my_list)):
        # print(i)
        smallest = findSmallest(my_list)
        # print(smallarr)
        new_list.append(my_list.pop(smallest))
        # print(new_list)
    return new_list




if __name__ == "__main__":
    my_list = [11,45,1,5,2,76,34,98,33]
    print(quickSorting(my_list))