class BinaryTree:
    def __init__(self, data, parent, left, right):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        
    def insert(self, tree, data, parent):
        if tree = NULL:
            self.__init__(self, data, parent, NULL, NULL)
        if self.data < parent.data:
            insert(self, tree.left, data, parent)
        else:
            insert(self, tree.right, data, parent)
    
    def delete(self, tree)
        
    def search_tree(tree, object):
        if tree == NULL: return NULL
        if tree.data == object: return tree
        if object < tree.data: 
            return search_tree(tree.left, object)
        else:
            return search_tree(tree.right, object)
            
    def find_min(tree):
        if tree == NULL: return NULL
        else:
            min = tree
            while min.left != NULL:
                min = min.left
            return min
    
    def find_max(tree):
        if tree == NULL: return NULL
        else:
            max = tree
            while max.right != NULL:
                max = max.right
            return max
    
    def traverse_tree(tree):
        if tree != NULL:
            traverse_tree(tree.left)
            process_item(tree.data)
            traverse_tree(tree.right) 