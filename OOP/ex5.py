class Node(object): 
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree(object): 
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None: 
            self.root = Node(value)
            return
        return self.insertNode(self.root, value)
    def insertNode(self, node, value):
        cur = node
        if value < cur.value:
            if cur.left == None:
                cur.left = Node(value)
                return 
            self.insertNode(cur.left, value)
        else:
            if cur.right == None:
                cur.right = Node(value)
                return
            self.insertNode(cur.right, value)

    def search(self, value):
        if self.root == value:
            True
        else:
            return self.searchNode(self.root, value)
    def searchNode(self, node, value):
        cur = node
        if value == cur.value:
            return True
        if value < cur.value:
            if cur.left == None:
                return False
            return self.searchNode(cur.left, value)
        else:
            if cur.right == None:
                return False
            return self.searchNode(cur.right, value)
bt = BinarySearchTree()
bt.insert(20)
bt.insert(10)
bt.insert(30)
print(bt.search(40))
            
    

