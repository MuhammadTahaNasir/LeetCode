class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int i = 0, j = 1;
        while (j < n) {
            if (nums[i] != nums[j]) { // Here We get unique number
                i++;
                nums[i]=nums[j];
            }
            j++;
        }
        return i + 1;
    }
};