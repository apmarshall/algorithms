def binary_search(key, list)
    l = len(list)
    if l = 0: return -1
    else:
        mid = l/2
        if list[mid] == key: return indexOf(list[mid])
        else:
            if list[mid] > key:
                return binary_search(key, list[0:mid])
            else:
                return binary_search(key, list[mid:])
