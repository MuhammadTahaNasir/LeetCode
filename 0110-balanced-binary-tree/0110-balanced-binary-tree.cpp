class Solution {
public:
    int check(TreeNode* node) {
        if (!node) return 0;
        int left = check(node->left);
        if (left == -1) return -1;
        int right = check(node->right);
        if (right == -1 || abs(left - right) > 1) return -1;
        return 1 + max(left, right);
    }
    bool isBalanced(TreeNode* root) {
        return check(root) != -1;
    }
};