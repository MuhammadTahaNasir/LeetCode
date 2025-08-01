class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        pascal = [[1]]
        for _ in range(1, numRows):
            prev = pascal[-1]
            # Build a new row by summing adjacent pairs from previous:
            # First and last elements are always 1
            row = [1] + [prev[j] + prev[j+1] for j in range(len(prev)-1)] + [1]
            pascal.append(row)
        return pascal
