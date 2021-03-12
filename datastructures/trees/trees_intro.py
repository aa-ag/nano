class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get_value(self):
        print(self.value)


# Check

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")

node0.get_value()
node1.get_value()
node2.get_value()
