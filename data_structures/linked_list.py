class Linked_List:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def search(list, item):
        if (list == empty) return NULL
        else:
            if list[0].data == item
                return 1
            else:
                return search(list[1:], item)
                
    def insert(list, item):
        __init__(self, item, list)
    
    def predecessor(list, item)
        if ((list == NULL) || (list[0].next == NULL)):
            return NULL
        else:
            if list[1].data == item:
                return 1
            else:
                return predecessor(list[1:], item)
            
    def delete(list, item):
        if search(list, item) != NULL:
            pred = predecessor(list, item)
            pred.next = item.next
    