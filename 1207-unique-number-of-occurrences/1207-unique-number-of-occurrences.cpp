class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        const int OFFSET = 1000;   // Offset to handle negative indices
        const int RANGE = 2001;    // Range from -1000 to 1000

        // Step 1: Count occurrences of each value in the array
        int count[RANGE] = {0};    // To count occurrences of each number

        for (int num : arr) {
            count[num + OFFSET]++;
        }

        // Step 2: Check if occurrence counts are unique
        // Use an array to track the frequencies of occurrence counts
        const int MAX_OCCURRENCES = 1001;  // Max occurrences possible
        bool freqSeen[MAX_OCCURRENCES] = {false};

        for (int i = 0; i < RANGE; ++i) {
            if (count[i] > 0) {  // If this number was seen
                if (freqSeen[count[i]]) {
                    return false;  // If this frequency has already been seen, return false
                }
                freqSeen[count[i]] = true;  // Mark this frequency as seen
            }
        }

        return true;  // All occurrence counts are unique
    }
};
