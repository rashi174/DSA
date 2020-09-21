#https://practice.geeksforgeeks.org/problems/level-order-traversal/1
#Given a binary tree, find its level order traversal.Level order traversal of a tree is breadth-first traversal for the tree.

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
# Your task is to complete this function
# Function should return the level order of the tree in the form of a list of integers
def levelOrder( root ):
    queue=[root]  #create a queue and add root of tree to it
    ans=[]  #create a list to return
    while len(queue)>0:  
        if queue[0].left:   
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)
        ans.append(queue.pop(0).data)
    return ans
