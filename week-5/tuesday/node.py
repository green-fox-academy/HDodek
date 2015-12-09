class Node:
    def __init__(self, value, left = Node, right = Node):
        self.value = value
        self.left = left
        self.right = right

root = Node(
    1,
    Node(2) #left
    Node(3) #right
)

class LeftIterator:
    def __init__(self, root):
        self.curr = root

    def next(self):
        self.curr = self.curr.left
        return self.curr is not None

    def current(self):
        return self.curr
