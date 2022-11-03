#!/usr/bin/python

def binary_search(my_list,item):
    
    low = 0
    high = len(my_list)-1 
    while low <= high:
        mid = int(((low + high)/2))
        guss = my_list[mid]
        # print(guss)
        # print(type(guss))
        if guss == item:
            return mid
        if guss > item:
            high = mid - 1 
        else:
            low =  mid + 1 
    return None

if __name__ == "__main__":
    my_list = [1,2,3,4,5,6,7,8,9]
    # print(binary_search(my_list,5))
    print(binary_search(my_list,9))
    print(binary_search(my_list,8))
    print(binary_search(my_list,7))
    print(binary_search(my_list,6))
    print(binary_search(my_list,5))
    print(binary_search(my_list,4))
    print(binary_search(my_list,3))
    print(binary_search(my_list,2))
    print(binary_search(my_list,1))