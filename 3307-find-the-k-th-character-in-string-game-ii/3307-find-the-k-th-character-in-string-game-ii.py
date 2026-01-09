class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1  # Convert to 0-based indexing
        increases = 0
        
        # Process operations from right to left
        for i in range(len(operations) - 1, -1, -1):
            segment_size = 1 << i  # 2^i, size of left half after i-th operation
            if k >= segment_size:
                k -= segment_size  # Move to left half
                if operations[i] == 1:
                    increases += 1
        
        return chr(ord('a') + (increases % 26))