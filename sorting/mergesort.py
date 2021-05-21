def mergesort(list)
    listLen = len(list)
    if (listLen > 1):
        middle = listLen/2
        l = mergesort(list[0:middle]
        r = mergesort(list[middle:-1]
        merge(l, r)
        
def merge(list1, list2)
    mergedList = []
    while ((len(list1) > 0) || (len(list2) > 0)):
        if (list1[0] >= list2[0]):
            mergedList += list1[0]
            merge(list1[1:], list2)
        else:
            mergedList += list2[0]
            merge(list1, list2[1:])
