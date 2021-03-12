class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get_value(self):
        print(self.value)

    def set_right_child(self, new_value):
        self.right = new_value

    def set_left_child(self, new_value):
        self.left = new_value

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None


# Create Binary Tree
class BinaryTree():
    def __init__(self):
        '''
         Class names should normally use the CapWords convention.
         https://www.python.org/dev/peps/pep-0008/#id41
        '''
        self.root = None

    def get_root(self):
        return self.root
