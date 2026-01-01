# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSame(self,l,r):
        
        if l==None and r ==None:
            return True
        elif l== None and r!=None :
            return False
        elif l!= None and r==None :
            return False
        return l.val==r.val and self.isSame(l.left, r.right) and self.isSame(l.right , r.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        l=root.left
        r=root.right

        return self.isSame(l, r)
        