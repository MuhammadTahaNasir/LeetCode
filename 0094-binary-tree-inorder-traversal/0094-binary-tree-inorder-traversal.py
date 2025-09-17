class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(node):
            if not node: return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        return res