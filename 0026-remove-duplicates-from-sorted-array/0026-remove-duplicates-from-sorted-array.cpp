class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        if (nums.empty()) return 0; // Handle the edge case of an empty array
        
        int i = 0; // `i` is the slow pointer

        for (int j = 1; j < nums.size(); j++) { // `j` is the fast pointer
            if (nums[j] != nums[i]) { // Found a unique element
                i++;
                nums[i] = nums[j]; // Move the unique element forward
            }
        }
        
        return i + 1; // Length of the array with unique elements
    }
};
