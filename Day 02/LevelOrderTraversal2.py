
#Level Order Traversal of a Binary Tree ---->>>from left to right
#Seprate each level by a $ symmbol      --->>>Level 1 $ Level 2 $ Level 3

#            10        Level1
#           / \
#          20  30      Level2
#         / \  / \
#        40 50 N  60   Level3
queue=[root]
level=[]
while (len(queue)>0):
    for i in range(0,len(queue)):
        if queue[0].left:
            nodes+=1
            queue.append(queue[0].left)
        if queue[0].right:
            nodes+=1
            queue.append(queue[0].right)
        level.append(queue.pop(0).data)
    level.append('$')
print(level)
