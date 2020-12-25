'''
498. Diagonal Traverse (Medium)
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
 

Note:

The total number of elements of the given matrix will not exceed 10,000.
'''

class Solution:
    def findDiagonalOrder(self, l: List[List[int]]) -> List[int]:
        d={}
        for i in range(len(l)):
            for j in range(len(l[0])):
                if i+j not in d:
                    d[i+j]=[l[i][j]]
                else:
                    d[i+j].append(l[i][j])
        result=[i for i in d.values()]
        for i in range(len(result)):
            if i%2==0:
                result[i]=result[i][::-1]
        return sum(result,[])
                    
