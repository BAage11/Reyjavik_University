
class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass



class BST_Node():
    def __init__(self, key = None, data = None, left = None, right = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BSTMap():
    def __init__(self):
        self.root = None
        self.size = 0


    def insert(self, key, data):
        """ Adds this value pair to the collection. 
            If equal key is already in the collection, 
            raise ItemExistsException(). """
        if self.root == None:
            self.root = BST_Node(key, data, None, None)
            self.size += 1
        else:
            self.insert_recursive(key, data, self.root)


    def insert_recursive(self, key, data, node):
        """ Check for an available spot in the tree, based on the key value. 
            If the key is smaller than the root key, it goes down the left subtree.
            If the key is larger than the root key, it goes down the right subtree. """
        if key < node.key:
            if node.left == None:
                node.left = BST_Node(key, data, None, None) 
                self.size += 1    
                return       
            return self.insert_recursive(key, data, node.left)
        elif key > node.key:
            if node.right == None:
                node.right = BST_Node(key, data, None, None)
                self.size += 1
                return
            return self.insert_recursive(key, data, node.right)
        else:
            raise ItemExistsException()


    def update(self, key, data):
        """ Sets the data value of the value pair with equal ​key to ​data. 
            If equal key is not in the collection, raise NotFoundException(). """
        curr_node = self.root
        while curr_node != None:
            if key == curr_node.key:
                curr_node.data = data
                return
            elif key > curr_node.key:
                curr_node = curr_node.right
            elif curr_node.key > key:
                curr_node = curr_node.left
        raise NotFoundException


    def find(self, key):
        """ Returns the ​data​ value of the value pair with equal ​key. 
            If equal key is not in the collection, raise NotFoundException(). """
        curr_node = self.root
        while curr_node != None:
            if curr_node.key == key:
                return curr_node.data
            elif key > curr_node.key:
                curr_node = curr_node.right
            elif curr_node.key > key:
                curr_node = curr_node.left
        raise NotFoundException()


    def recursive_contain(self, key, node):
        """ Search the tree, looking up the key value for each node.
            If key is found in node, return True, else False. """
        if node == None:
            return False
        elif node.key == key:
            return True

        if key < node.key:
            return self.recursive_contain(key, node.left)
        elif key > node.key:
            return self.recursive_contain(key, node.right)


    def contains(self, key):
        """  Returns ​True​ if equal ​key​ is found in the collection, 
            otherwise ​False. """
        return self.recursive_contain(key, self.root)


    def remove(self, key):
        """ Removes the value pair with equal ​key​ from the collection. 
            If equal key is not in the collection, raise NotFoundException(). """
        # empty tree
        if self.root == None:
            raise NotFoundException()

        # key is in root node
        elif self.root.key == key:
            if self.root.left is None and self.root.right is None:
                self.root = None      # tree becomes empty
            elif self.root.left and self.root.right is None:
                self.root = self.root.left      # left node becomes root
            elif self.root.left is None and self.root.right:
                self.root = self.root.right     # right node becomes root
            elif self.root.left and self.root.right:
                delNodeParent = self.root         
                delNode = self.root.right
                while delNode.left:
                    # look for the smallest value in the right-child nodes from root
                    delNodeParent = delNode
                    delNode = delNode.left
                # smallest right-child of root has been found (delNode)

                self.root.key, delNode.key = delNode.key, self.root.key
                # swap smallest 'right-child' of root, with root
                if delNode.right:
                # If 'new' root had a right child, swap and delete 'old' root with it
                    delNode.key, delNode.right.key = delNode.right.key, delNode.key
                    delNode.right = None
        
            self.size -= 1
            return  # key removed successfully

        # ... else, look for the key value in subtrees of root
        parent = None
        node = self.root

        # start by finding key/node to be removed
        while node and node.key != key:     
        # while node is not 'None' or not key being looked for...
            parent = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
        # 'node' is None or key has been found in tree

        # if key was not found (node == 'None')
        if node is None or node.key != key:
            raise NotFoundException()

        # if key being removed has no children
        elif node.left is None and node.right is None:
            if key < parent.key:
            # deletes/removes the key in accordance to key's parent value
                parent.left = None
            else:
                parent.right = None
            self.size -= 1
            return  # key removed successfully
            
        # key removed has left-child only
        elif node.left and node.right is None:
            if key < parent.key:
                # the key being deleted is a left node, and the child inherits its parent (spot)
                parent.left = node.left
            else:
                # the key being deleted is a right node, and the child inherits its parent (spot)
                parent.right = node.left
            self.size -= 1
            return  # key removed successfully

        # remove node has right-child only
        elif node.left is None and node.right:
            if key < parent.key:
                # the key being deleted is a left node, and the child inherits its parent (spot)
                parent.left = node.right
            else:
                # the key being deleted is a right node, and the child inherits its parent (spot)
                parent.right = node.right
            self.size -= 1
            return  # key removed successfully

        # key being removed has both left-child and right-child
        else:
            delNodeParent = node       # key that is being removed
            delNode = node.right       
            # must find the smallest child of key (that is being removed) right child
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left
            # smallest child of the 'right subtree' has been found (delNode)

            node.key, delNode.key = delNode.key, node.key
            # swap the values of smallest child and the key that is being deleted

            if delNode.right:  
            # checking if right child of the key being deleted exists
                if delNodeParent.key > delNode.key:
                # if parent of key being deleted is larger, key being deleted is a left-child, and right-child of the key being deleted inherits its parent (the deleted node)
                    delNodeParent.left = delNode.right
                elif delNodeParent.key > delNode.key:
                # else the deleted node is a right-child, and the right-child of the deleted key inherits its parent
                    delNodeParent.right = delNode.right
                return  # key removed successfully

            else:
            # if right child of key being deleted is non-existing ....
                if delNode.key < delNodeParent.key:
                # if key being deleted is smaller than its parent, it is a left child and therefore that child == 'None'
                    delNodeParent.left = None
                else:
                # ... but if it is larger than its parent, it is a right child and that becomes 'None' so the key is deleted 
                    delNodeParent.right = None
                self.size -= 1
                return  # key removed successfully


    def __setitem__(self, key, data):
        """ Override to allow this syntax:  some_bst_map[key] = data 
            If equal ​key is already in the collection, update its ​data value. 
            Otherwise add the value pair to the collection. """
        curr_node = self.root
        while curr_node != None:
            if curr_node.key == key:
                curr_node.data = data
                return
            elif curr_node.key > key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        self.insert(key, data)


    def __getitem__(self, key):
        """ Override to allow this syntax:  my_data = some_bst_map[key] 
            Returns the ​data​ value of the value pair with equal ​key. 
            If equal key is not in the collection, raise NotFoundException(). """
        curr_node = self.root
        while curr_node != None:
            if curr_node.key == key:
                return curr_node.data
            elif curr_node.key > key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        raise NotFoundException()


    def __len__(self):
        """ Override to allow this syntax:  length_of_structure = len(some_bst_map)
            Returns the number of items in the entire data structure. """
        return self.size


    def print_inorder(self, node):
        """ Prints tree value from smallest to largest. """
        if node == None:
            return ""
        return "{} {} {}".format(self.print_inorder(node.left), "{" + str(node.key) + ":" + str(node.data) + "}", self.print_inorder(node.right))


    def __str__(self):
        """ Returns a string with the items ​ordered​ by ​key and separated by a single         space. Each item is printed on the following format: 
            {value_of_key:value_of_data}. """ 
        return self.print_inorder(self.root)


m = BSTMap()

m[5] = "five"
m[3] = "three"
m[7] = "seven"

print(m)