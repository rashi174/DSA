#Level Order Traversal of a Binary Tree ---->>>from left to right
#Store each level in a seprate list return a list of all lists(2D List)

#            10        Level1
#           / \
#          20  30      Level2
#         / \  / \
#        40 50 N  60   Level3

#[[10],[20,30],[40,50,60]]

def levelOrder(root):
    '''
    :param root: root of given tree.
    :return: the level order traversal 
    '''
    # code here
    queue=[root]
    ans=[]
    while (len(queue)>0):
        templ=[]
        for i in range(0,len(queue)):
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            templ.append(queue.pop(0).data)
        ans.append(templ)
    return ans
