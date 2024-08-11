class Solution {
private:
    const vector<vector<int>> DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

public:
    int minDays(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        // Check initial number of islands
        int initialIslandCount = countIslands(grid);
        if (initialIslandCount != 1) {
            return 0;  // Already disconnected or no land
        }

        // Try removing each land cell and check the result
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == 0) continue;  // Skip water

                // Temporarily change to water
                grid[row][col] = 0;

                // Check the number of islands after removal
                int newIslandCount = countIslands(grid);

                // Revert the change
                grid[row][col] = 1;

                // If disconnected by removing this cell
                if (newIslandCount != 1) {
                    return 1;
                }
            }
        }

        // If no single cell removal leads to disconnection, return 2
        return 2;
    }

private:
    int countIslands(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int islandCount = 0;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == 1) {
                    if (++islandCount > 1) return islandCount;  // Early termination if more than one island is found
                    dfs(grid, row, col);
                }
            }
        }

        // Restore the grid by resetting marked cells
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == -1) {
                    grid[row][col] = 1;
                }
            }
        }

        return islandCount;
    }

    void dfs(vector<vector<int>>& grid, int row, int col) {
        grid[row][col] = -1;  // Mark as visited by changing the value

        for (const auto& direction : DIRECTIONS) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];

            if (isValidLandCell(grid, newRow, newCol)) {
                dfs(grid, newRow, newCol);
            }
        }
    }

    bool isValidLandCell(const vector<vector<int>>& grid, int row, int col) {
        int rows = grid.size();
        int cols = grid[0].size();
        return row >= 0 && col >= 0 && row < rows && col < cols && grid[row][col] == 1;
    }
};
