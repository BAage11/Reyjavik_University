class BST_Node():
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class ADT():
    def __init__(self):
        self.parent = None
        self.size = 0


    def add(self, value):
        """ Adds an item to the set with this value.
            If the value is already there, do nothing. """
        if self.parent == None:
            self.parent = BST_Node(value, None, None)
            self.size += 1
        else:
            self.add_recursive(value, self.parent)

    def add_recursive(self, value, node):
        if node.value == value:
            return
        if value < node.value:
            if node.left == None:
                node.left = BST_Node(value, None, None) 
                self.size += 1           
            return self.add_recursive(value, node.left)
        elif value > node.value:
            if node.right == None:
                node.right = BST_Node(value, None, None)
                self.size += 1
            return self.add_recursive(value, node.right)

    def recursive_contain(self, value, node):
        if node == None:
            return False
        elif node.value == value:
            return True

        if value < node.value:
            return self.recursive_contain(value, node.left)
        elif value > node.value:
            return self.recursive_contain(value, node.right)

    def contains(self, value):
        """ Returns True if a value is in the set, otherwise False. """
        return self.recursive_contain(value, self.parent)


    def __len__(self):
        """  Returns the number of items in the set. """
        return self.size


    def print_preorder(self, node):
        """ Prints all tree values preordered: 'node-left-right'. """
        if node == None:
            return ""
        return "{} {} {}".format(node.value, self.print_preorder(node.left), self.print_preorder(node.right))


    def print_postorder(self, node):
        """ Prints tree values postordered: 'left-node-right' and the root at last. """
        if node == None:
            return ""
        return "{} {} {}".format(self.print_postorder(node.left), self.print_postorder(node.right), node.value)


    def print_inorder(self, node):
        """ Prints tree value from smallest to largest."""
        if node == None:
            return ""
        return "{} {} {}".format(self.print_inorder(node.left), node.value, self.print_inorder(node.right))


    def __str__(self):
        """ Prints the contents of the tree, ordered. """
        return self.print_inorder(self.parent)        
        


bst = ADT()
bst.add(7)
bst.add(5)
bst.add(3)
bst.add(6)
bst.add(9)
bst.add(8)
bst.add(11)
print("Inorder:", bst)
print("Postorder:", bst.print_postorder(bst.parent))
print("Preorder:", bst.print_preorder(bst.parent))

print("Value 5 in tree:", bst.contains(5))
print("Value 15 in tree:", bst.contains(15))
print("Size of tree:", len(bst))