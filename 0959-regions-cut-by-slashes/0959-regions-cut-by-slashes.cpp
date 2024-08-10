class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int gridSize = grid.size();
        int n = gridSize * 3; // Scale up the grid

        // Create a visited grid
        vector<vector<int>> visited(n, vector<int>(n, 0));
        int regions = 0;

        // Iterate through the scaled grid and run DFS on unvisited cells
        for (int i = 0; i < gridSize; ++i) {
            for (int j = 0; j < gridSize; ++j) {
                // Scale the grid
                int r = i * 3;
                int c = j * 3;

                if (grid[i][j] == '/') {
                    visited[r][c + 2] = 1;
                    visited[r + 1][c + 1] = 1;
                    visited[r + 2][c] = 1;
                } else if (grid[i][j] == '\\') {
                    visited[r][c] = 1;
                    visited[r + 1][c + 1] = 1;
                    visited[r + 2][c + 2] = 1;
                }
            }
        }

        // Perform DFS to find regions
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (!visited[i][j]) {
                    dfs(visited, i, j, n);
                    ++regions;
                }
            }
        }

        return regions;
    }

private:
    void dfs(vector<vector<int>>& visited, int i, int j, int n) {
        if (i < 0 || i >= n || j < 0 || j >= n || visited[i][j]) {
            return;
        }

        visited[i][j] = 1;
        dfs(visited, i + 1, j, n); // Down
        dfs(visited, i - 1, j, n); // Up
        dfs(visited, i, j + 1, n); // Right
        dfs(visited, i, j - 1, n); // Left
    }
};
