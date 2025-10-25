class Solution {
public:
    int hammingDistance(int x, int y) {
        int val = x ^ y;
        int dist = 0;
        while (val) {
            dist++;
            val &= val - 1;
        }
        return dist;
    }
};