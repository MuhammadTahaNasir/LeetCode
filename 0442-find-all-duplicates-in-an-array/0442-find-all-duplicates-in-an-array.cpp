class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> result;
        
        for (int i = 0; i < nums.size(); ++i) {
            int index = abs(nums[i]) - 1;
            
            // If the number at this index is negative, it means the number has been seen before
            if (nums[index] < 0) {
                result.push_back(index + 1);
            } else {
                // Mark the number as seen by negating the value at that index
                nums[index] = -nums[index];
            }
        }
        
        return result;
    }
};