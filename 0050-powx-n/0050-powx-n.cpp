class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1.0;
        if (x == 1.0) return 1.0;  // Edge case for base 1
        if (x == -1.0) return (n % 2 == 0) ? 1.0 : -1.0; // Edge case for base -1

        long num = n;
        double pow = 1.0;

        if (n < 0) {
            num = -num;
            x = 1 / x;
        }

        while (num > 0) {
            if (num & 1) {
                pow *= x;
            }
            x *= x;
            num >>= 1;
        }

        return pow;
    }
};