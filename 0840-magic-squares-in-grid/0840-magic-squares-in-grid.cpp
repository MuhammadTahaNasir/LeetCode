class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int ans = 0;

        for (int i = 0; i + 2 < grid.size(); ++i) {
            for (int j = 0; j + 2 < grid[0].size(); ++j) {
                if (grid[i + 1][j + 1] == 5 && isMagic(grid, i, j)) {
                    ans++;
                }
            }
        }

        return ans;
    }

private:
    bool isMagic(const vector<vector<int>>& grid, int i, int j) {
        // Check if the numbers are distinct and within the range 1-9
        int vals[10] = {0};  // Track digits from 1 to 9

        for (int r = 0; r < 3; ++r) {
            for (int c = 0; c < 3; ++c) {
                int num = grid[i + r][j + c];
                if (num < 1 || num > 9 || ++vals[num] > 1) {
                    return false;
                }
            }
        }

        // Check rows, columns, and diagonals sums
        return (grid[i][j] + grid[i][j + 1] + grid[i][j + 2] == 15 &&
                grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] == 15 &&
                grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2] == 15 &&
                grid[i][j] + grid[i + 1][j] + grid[i + 2][j] == 15 &&
                grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1] == 15 &&
                grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2] == 15 &&
                grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] == 15 &&
                grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] == 15);
    }
};
