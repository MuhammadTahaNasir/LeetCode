class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> output(n, 1);
        int left = 1, right = 1;

        for (int i = 0; i < n; ++i) {
            output[i] *= left;       // Multiply with left-side products
            output[n - 1 - i] *= right; // Multiply with right-side products
            left *= nums[i];
            right *= nums[n - 1 - i];
        }

        return output;
    }
};