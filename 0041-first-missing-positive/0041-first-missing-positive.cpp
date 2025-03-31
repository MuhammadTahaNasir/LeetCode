class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();

        // Step 1: Replace non-positive numbers and numbers greater than n with 1.
        bool contains1 = false;
        for (int& num : nums) {
            if (num == 1) contains1 = true;
            if (num <= 0 || num > n) num = 1;
        }
        if (!contains1) return 1;

        // Step 2: Use the index as a hash key and mark the presence of each number.
        for (int i = 0; i < n; i++) {
            int idx = abs(nums[i]) - 1;
            if (nums[idx] > 0) nums[idx] = -nums[idx];
        }

        // Step 3: The first positive index + 1 is the missing number.
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) return i + 1;
        }

        return n + 1;
    }
};