# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def m_depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            r = m_depth(root.right)
            l = m_depth(root.left)


            return max(l,r) + 1
        
        return m_depth(root)