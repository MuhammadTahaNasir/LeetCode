class Solution {
public:
    bool isPalindrome(int x) {
        // A negative number cannot be a palindrome.
        // Also, if the last digit of the number is 0, the first digit must also be 0 (which is not possible unless the number is 0).
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int reversedHalf = 0;
        while (x > reversedHalf) {
            // Add the last digit of x to reversedHalf
            reversedHalf = reversedHalf * 10 + x % 10;
            // Remove the last digit from x
            x /= 10;
        }

        // When the length is odd, we can remove the middle digit by reversedHalf / 10
        return x == reversedHalf || x == reversedHalf / 10;
    }
};