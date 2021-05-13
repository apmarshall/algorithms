import Linked_List as ll

reversed_list = NULL

def reverse(list):
    new_next = list
    new_pred = list.next
    if new_pred = NULL:
        return reversed_list
    else:    
        reversed_list += ll.insert(this, new_pred, new_next)
        return reverse(new_pred)