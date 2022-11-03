from unittest import result


def recurrence(arr):
    new_num = arr -1 
    if new_num >= 1:
        result = arr * recurrence(new_num)
    else:
        return 1

    return result 

if __name__ == "__main__":
    print(recurrence(100))
