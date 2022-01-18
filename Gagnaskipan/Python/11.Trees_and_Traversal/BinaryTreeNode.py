
class BinaryTreeNode():
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self):
        self.root = None

    def _populate_tree_recur(self, position):
        data_str = input("Current position: {}\nInsert value:  ".format(position))
        if data_str == "":
            return None
        return BinaryTreeNode(data_str, self._populate_tree_recur(position + " left"), self._populate_tree_recur(position + " right"))

    def populate_tree(self):
        self.root = self._populate_tree_recur("root")

    def _print_tree_recur(self, node):
        if node == None:
            return
        print(str(node.data), end=" ")
        self._print_tree_recur(node.left)
        self._print_tree_recur(node.right)

    def print_tree(self):
        self._print_tree_recur(self.root)
        print()


if __name__ == "__main__":
    bt = BinaryTree()
    bt.populate_tree()
    bt.print_tree()

