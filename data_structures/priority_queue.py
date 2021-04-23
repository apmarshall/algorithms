class Priority_Queue:
    def __init__(this, data, num):
        this.data = data
        this.num = num
    
    def find_parent(num):
        if num == 1: return -1
        else: return num/2
        
    def find_left_child(num):
        return num*2
        
    def find_right_child(num):
        return (num*2)+1
    
    def insert(queue, item):
        num = len(queue) + 1
        newQ = new(PriorityQueue(this, item, num)
        bubble_up(newQ)
        
    def bubble_up(item):
        parent = find_parent(item.num)
        if parent == -1: return
        else:
            if parent.data > item.data:
                pq_swap(parent, item)
                bubble_up(item)
    
    def remove_item(queue, item):
        num = item.num
        cand = 0
        if num == 0
            cand = len(queue)
        else:
            subqueue_depth = lg(len(queue[num:]))
            cand = num * pow(2, subqueue_depth) + subqueue_depth
        if num <= 0: return
        else:
            pq_swap(item, cand)
            bubble_down(cand)
            
    def extract_min(queue):
        min = queue[0]
        remove_item(queue, queue[0])
        return min
        
    def bubble_down(item):
        right = find_right_child(item)
        left = find_left_child(item)
        
        if item.data > right.data:
            pq_swap(item, right)
            bubble_down(item)
        if item.data > left.data:
            pq_swap(item, left)
            bubble_down(item)
    
    def pq_swap(item1, item2)
        
             