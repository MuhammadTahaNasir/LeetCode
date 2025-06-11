class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_len = 0, curr = 0;
        for (int x : nums) {
            if (x == 1) {
                curr++;
                max_len = max(max_len, curr);
            } else curr = 0;
        }
        return max_len;
    }
};