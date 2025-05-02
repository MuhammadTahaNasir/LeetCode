class Solution {
public:
    void helper(TreeNode* node, string path, vector<string>& res) {
        if (!node) return;
        if (!node->left && !node->right) {
            res.push_back(path + to_string(node->val));
            return;
        }
        helper(node->left, path + to_string(node->val) + "->", res);
        helper(node->right, path + to_string(node->val) + "->", res);
    }
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        helper(root, "", res);
        return res;
    }
};