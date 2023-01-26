from binarytree import Node

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order(self):
        elements = []
        if self.left:
            elements += self.left.in_order()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order()

        return elements

    def pre_order(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order()

        if self.right:
            elements += self.right.pre_order()

        return elements

    def post_order(self):
        elements = []
        if self.left:
            elements += self.left.pre_order()

        if self.right:
            elements += self.right.pre_order()
        
        elements.append(self.data)

        return elements
        
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
    print(elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

print("\nVIENNE KAYETTE LARESMA JAVIER\n")
print("Building tree with these elements:", ["V", "I", "E", "N", "N", "E", "K", "A", "Y","E", "T", "T", "E","L", "A", "R", "E", "S", "M", "A", "J", "A", "V", "I", "E", "R"])

root = Node("V")
root.left = Node("I")
root.right = Node("Y")
root.left.left = Node("E")
root.left.right = Node("N")
root.left.right.left = Node("K")
root.left.right.right = Node("T")
root.left.right.right.left = Node("S")
root.left.right.right.left.left = Node("R")
root.left.right.left.left = Node("J")
root.left.right.left.right = Node("L")
root.left.right.left.right.right = Node("M")
root.left.left.left = Node("A")
print(root)

if __name__ == "__main__":
    vkj_tree = build_tree(["V", "I", "E", "N", "N", "E", "K", "A", "Y","E", "T", "T", "E","L", "A", "R", "E", "S", "M", "A", "J", "A", "V", "I", "E", "R"])
    print("\nIn order traversal:", vkj_tree.in_order()) 
    print("Pre order traversal:", vkj_tree.pre_order())
    print("Post order traversal:", vkj_tree.post_order())

    vkj_tree.delete("K")
    print("\nAfter deleting the letter 'K':\nIn order traversal:", vkj_tree.in_order(), "\nPre order traversal:", vkj_tree.pre_order(), "\nPost order traversal:", vkj_tree.post_order())

    print("\nDoes the name contain the letter J?", vkj_tree.search("J"))
    print("Does the name contain the letter P?", vkj_tree.search("P"))