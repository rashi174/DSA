'''
52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9

'''

res,l=[],[]
class Solution:
    def __init__(self):
        global res
        res=[]
    
    def Createboard(self,n):
        #board banenge
        board=[['.']*n for i in range(n)]
        return board
    
    def totalNQueens(self, n: int) -> List[List[str]]:
        global res
        board=self.Createboard(n)
        self.nQueens(board,0,n)
        return len(res)

    def nQueens(self,board,row,n):
        global res
        list1=[]
        if row==n:
            for i in range(n):
                temp=''.join(board[i])
                list1.append(temp)
            res.append(list1)
            return
        for col in range(n):
            if self.isSafe(board,row,col,n):
                board[row][col]='Q' #place Queen here !!!
                self.nQueens(board,row+1,n)
                board[row][col]='.' #remove queen / backtrack
                
    def isSafe(self,arr,x,y,n):
        for row in range(x):
            if arr[row][y]=='Q':
                return False
        row=x
        col=y
        while (row>=0 and col>=0):
            if (arr[row][col]=='Q'):
                return False
            row-=1
            col-=1
    
        row=x
        col=y
        while (row>=0 and col<n):
            if (arr[row][col]=='Q'):
                return False
            row-=1
            col+=1
        return True
            
            
        
        
