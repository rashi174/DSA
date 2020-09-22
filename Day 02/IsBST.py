
#https://practice.geeksforgeeks.org/problems/check-for-bst/1
#Given a binary tree. Check whether it is a BST or not.


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# return True if the given tree is a BST, else return False
def isBST(root):
    #code here
    def inorder(root):
        list1=[]
        if root:
            list1.extend(inorder(root.left))
            list1.append(root.data)
            list1.extend(inorder(root.right))
        return list1
    inordertraversal=inorder(root)
    for i in range(len(inordertraversal)-1):
        if inordertraversal[i]>=inordertraversal[i+1]:
            return False
    return True