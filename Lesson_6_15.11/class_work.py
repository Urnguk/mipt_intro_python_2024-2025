class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.v = value
        self.p = parent
        self.l = left
        self.r = right

class SearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            curr_node = self.root
            while True:
                if value < curr_node.v:
                    if curr_node.l is None:
                        curr_node.l = Node(value, curr_node)
                        return
                    curr_node = curr_node.l
                else:
                    if curr_node.r is None:
                        curr_node.r = Node(value, curr_node)
                        return
                    curr_node = curr_node.r

    def get_sorted_list(self, curr_node="start"):
        if curr_node == "start":
            curr_node = self.root
        if curr_node is None:
            return []
        return (self.get_sorted_list(curr_node.l) +
                [curr_node.v] +
                self.get_sorted_list(curr_node.r))


bt = SearchTree()
A = [2, 6, 0, -1, 4, 7, -9]
for element in A:
    bt.add(element)
B = bt.get_sorted_list()
print(*B)



