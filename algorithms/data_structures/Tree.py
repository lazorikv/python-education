"""Module to represent Tree"""


class Node:
    """class to represent each node of the Tree"""
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:
    """Class realized methods for Tree"""

    def createNode(self, data):
        """function to create a node"""
        return Node(data)

    def insert(self, node, data):
        """Insert function will insert a node into tree"""

        #  if tree is empty, return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side,
        # if data bigger - to right side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node

    def deleteNode(self, node, data):
        """Delete function will delete a node into tree"""

        # Check if tree is empty
        if node is None:
            return None

        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else:
            if node.left is None and node.right is None:
                del node
            if node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp

        return node

    def search(self, node, data):
        """Search function will search a node into tree"""

        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def traverseInorder(self, t_root):
        """shows the trunk for all branches"""
        if t_root is not None:
            self.traverseInorder(t_root.left)
            print(t_root.data)
            self.traverseInorder(t_root.right)

    def traversePreorder(self, p_root):
        """traverse function will print all tree in order of nesting"""
        if p_root is not None:
            print(p_root.data)
            self.traversePreorder(p_root.left)
            self.traversePreorder(p_root.right)

    def traversePostorder(self, po_root):
        """traverse function will print all the node in the tree in reverse order"""
        if po_root is not None:
            self.traversePostorder(po_root.left)
            self.traversePostorder(po_root.right)
            print(po_root.data)


root = None
tool = None
custom_tree = Tree()
root = custom_tree.insert(root, 100)
tool = custom_tree.insert(tool, 4)
custom_tree.insert(root, 200)
custom_tree.insert(root, 300)
custom_tree.insert(root, 400)
custom_tree.insert(root, 700)
custom_tree.insert(root, 600)
custom_tree.insert(root, 550)
custom_tree.insert(root, 800)
print("Traverse Inorder")
custom_tree.traverseInorder(root)
print("Traverse Preorder")
custom_tree.traversePreorder(root)
print("Traverse Postorder")
custom_tree.traversePostorder(root)
