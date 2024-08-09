class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Create a vector of pairs where each pair is (num, index)
        vector<pair<int, int>> num_indices;
        for (int i = 0; i < nums.size(); ++i) {
            num_indices.push_back({nums[i], i});
        }

        // Sort the pairs based on the number values
        sort(num_indices.begin(), num_indices.end());

        // Initialize two pointers
        int left = 0;
        int right = nums.size() - 1;

        // Use the two-pointer technique to find the target sum
        while (left < right) {
            int sum = num_indices[left].first + num_indices[right].first;
            if (sum == target) {
                return {num_indices[left].second, num_indices[right].second};  // Return original indices
            } else if (sum < target) {
                ++left;  // Move left pointer to the right
            } else {
                --right;  // Move right pointer to the left
            }
        }

        return {};  // Return empty vector if no solution is found
    }
};