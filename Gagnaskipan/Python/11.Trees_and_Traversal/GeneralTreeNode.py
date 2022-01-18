
class GeneralTreeNode():
    def __init__(self, data = None):
        self.data = data
        self.children = []

class GeneralTree():
    def __init__(self):
        self.root = None

    def _populate_tree_recur(self, position):
        data_str = input("Current position: {}\nInsert value:  ".format(position))
        if data_str == "":
            return None
        node = GeneralTreeNode(data_str)
        while True:
            child_node = self._populate_tree_recur(position + " child")
            if child_node == None:
                break
            node.children.append(child_node)  
        return node      

    def populate_tree(self):
        self.root = self._populate_tree_recur("root")

    def _print_tree_recur(self, node):
        if node == None:
            return
        print(str(node.data), end=" ")
        for child_node in node.children:
            self._print_tree_recur(child_node)

    def print_tree(self):
        self._print_tree_recur(self.root)
        print()


if __name__ == "__main__":
    gt = GeneralTree()
    gt.populate_tree()
    gt.print_tree()

