class Solution {
public:
    int countPrimes(int n) {
        if (n < 3) return 0;

        // Using a vector<bool> for space optimization
        vector<bool> isPrime(n, true);

        int result = n / 2; // Start with all odd numbers as primes (except 1)

        // Skip even numbers, starting from 3
        for (int i = 3; i * i < n; i += 2) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i * 2) {
                    if (isPrime[j]) {
                        isPrime[j] = false;
                        result--;
                    }
                }
            }
        }

        return result;
    }
};
