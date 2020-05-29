from LAB5 import *

if __name__ == "__main__":
    fname = "websites.txt"

    print("--- Constructing BST ---")
    construct_flag = True
    try:
        bst = constructBST(fname)
        print("No syntax or runtime errors occured in constructBST.")
        print("Root: " + str(bst.root))
    except:
        print("Could not construct BST.")
        construct_flag = False

    if construct_flag:
        print("--- Basic Traversal Check ---")
        print("Leftmost traversal: ")
        curr_node = bst.root
        while curr_node != None:
            curr_node = curr_node.left
            print(curr_node)

        print("Rightmost traversal: ")
        curr_node = bst.root
        while curr_node != None:
            curr_node = curr_node.right
            print(curr_node)

        print("Basic traversal check complete.")

    print("Tester complete.")
