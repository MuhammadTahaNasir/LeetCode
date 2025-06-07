class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(node):
            if not node: return
            helper(node.left)
            helper(node.right)
            res.append(node.val)
        helper(root)
        return res