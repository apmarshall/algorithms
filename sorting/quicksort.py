def quicksort(list):
    if len(list) > 0:
        p = partition(list)
        quicksort(list[0:p-1])
        quicksort(list[p+1:-1])
        
def partion(list)
    h = len(list)
    p = indexOf(list[-1])
    test = 1
    for j in range h:
        if (list[i] < list[p]:
            temp = list[test]
            list[test] = list[i]
            list[i] = temp
            test++
    temp = list[test]
    list[test] = list[p]
    list[p] = list[test]
    
    return indexOf(list[test])
