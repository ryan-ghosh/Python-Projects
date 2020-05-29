from time import perf_counter

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self, root):
        self.root = root
    def insert(self, node):
        curr = self.root
        if curr is None:
            curr = node
        if curr.__str__() > node.__str__():                     ## if curr is less than node
            if curr.left is None:
                curr.left = node
            else:
                BinarySearchTree(curr.left).insert(node)
        if curr.__str__() < node.__str__():                               ## if curr is greater than node
            if curr.right is None:
                curr.right = node
            else:
                BinarySearchTree(curr.right).insert(node)

    def search(self, val):
        curr = self.root
        if curr is None:
            return False
        if curr.__str__() == val:
            return True
        else:
            if curr.__str__() < val:
                return BinarySearchTree(curr.right).search(val)
            if curr.__str__() > val:
                return BinarySearchTree(curr.left).search(val)

def constructBST(filename):
    file_name = open(filename, 'r')
    line = file_name.readlines()
    for i in range(len(line)):
        line[i] = line[i].strip('\n')
    bruh = Node(line[0])
    bst = BinarySearchTree(bruh)
    for i in range(1, len(line)):
        bst.insert(Node(line[i]))
    return bst

if __name__ == "__main__":
    tree1 = constructBST('websites.txt')
    t1_start = perf_counter()
    print(tree1.search('cnn'))
    t1_stop = perf_counter()
    print('Elapsed time:', t1_stop - t1_start)