# Task 02: add a constructor that takes the value as a parameter
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


# tests
node0 = Node()
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")

node0 = Node("apple")
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")
