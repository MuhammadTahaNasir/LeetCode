class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) return x;
        int l = 2, r = x / 2, ans = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            long long num = (long long)mid * mid;
            if (num == x) return mid;
            else if (num < x) {
                ans = mid;
                l = mid + 1;
            } else r = mid - 1;
        }
        return ans;
    }
};