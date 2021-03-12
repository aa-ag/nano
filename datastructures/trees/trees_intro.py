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


# Check
node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

print("adding left and right children")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

print(f"""
node 0: {node0.value}
node 0 left child: {node0.left.value}
node 0 right child: {node0.right.value}
""")
