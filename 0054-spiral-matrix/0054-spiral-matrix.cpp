class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return {};

        int rows = matrix.size();
        int cols = matrix[0].size();
        vector<int> result;
        result.reserve(rows * cols);

        // Define boundaries
        int top = 0, bottom = rows - 1;
        int left = 0, right = cols - 1;

        // Traverse the matrix in spiral order
        while (top <= bottom && left <= right) {
            // Traverse from left to right across the top row
            for (int col = left; col <= right; col++) {
                result.push_back(matrix[top][col]);
            }
            top++;

            // Traverse from top to bottom down the right column
            for (int row = top; row <= bottom; row++) {
                result.push_back(matrix[row][right]);
            }
            right--;

            // Check if there's still a bottom row to traverse
            if (top <= bottom) {
                // Traverse from right to left across the bottom row
                for (int col = right; col >= left; col--) {
                    result.push_back(matrix[bottom][col]);
                }
                bottom--;
            }

            // Check if there's still a left column to traverse
            if (left <= right) {
                // Traverse from bottom to top up the left column
                for (int row = bottom; row >= top; row--) {
                    result.push_back(matrix[row][left]);
                }
                left++;
            }
        }

        return result;
    }
};
