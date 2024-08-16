class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        // Initialize global min and max with the first array's min and max
        int globalMin = arrays[0][0];
        int globalMax = arrays[0].back();
        int result = 0;

        // Iterate through the rest of the arrays
        for (int i = 1; i < arrays.size(); ++i) {
            // Get the local min and max for the current array
            int localMin = arrays[i][0];
            int localMax = arrays[i].back();

            // Calculate the maximum possible distance using the current array
            result = max(result, max(abs(localMax - globalMin), abs(globalMax - localMin)));

            // Update global min and max
            globalMin = min(globalMin, localMin);
            globalMax = max(globalMax, localMax);
        }

        return result;
    }
};
