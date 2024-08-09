class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> result;
        
        // Iterate through each number in the array
        for (int num : nums) {
            int index = abs(num) - 1;
            
            // Check if the value at this index has been negated (indicating a duplicate)
            if (nums[index] < 0) {
                result.push_back(index + 1);
            } else {
                // Negate the value at this index to mark the number as seen
                nums[index] = -nums[index];
            }
        }
        
        return result;
    }
};