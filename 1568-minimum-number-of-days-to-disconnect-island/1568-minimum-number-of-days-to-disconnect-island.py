class Solution:
    def minDays(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        # Function to count islands using DFS
        def countIslands(grid):
            def dfs(r, c):
                grid[r][c] = -1  # Mark cell as visited by setting it to -1
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        dfs(nr, nc)
            
            island_count = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        island_count += 1
                        if island_count > 1:
                            return island_count
                        dfs(r, c)
            
            # Restore the grid by setting -1 back to 1
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == -1:
                        grid[r][c] = 1
            
            return island_count
        
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        initial_islands = countIslands(grid)
        if initial_islands != 1:
            return 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                grid[r][c] = 0  # Temporarily change land to water
                if countIslands(grid) != 1:
                    return 1
                grid[r][c] = 1  # Revert the change
        
        return 2  # Return 2 if no single cell removal disconnects the land
