# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total = 0
        stack = [(root, 0)]
        
        while stack:
            node, current = stack.pop()
            
            # Build binary number
            current = (current << 1) | node.val
            
            # If leaf node
            if not node.left and not node.right:
                total += current
            else:
                if node.right:
                    stack.append((node.right, current))
                if node.left:
                    stack.append((node.left, current))
        
        return total