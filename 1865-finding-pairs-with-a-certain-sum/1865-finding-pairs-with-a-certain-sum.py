class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # Store nums1 and nums2, and create a Counter for nums2 to track frequencies of elements in nums2
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts2 = Counter(nums2)  # Frequency count of elements in nums2
        self.counts1 = Counter(nums1)  # Frequency count of elements in nums1

    def add(self, index: int, val: int) -> None:
        # Get the old value in nums2 at the given index
        old_val = self.nums2[index]
        # Decrease count for the old value
        self.counts2[old_val] -= 1
        if self.counts2[old_val] == 0:
            del self.counts2[old_val]
        
        # Update the value in nums2
        self.nums2[index] += val
        new_val = self.nums2[index]
        # Increase count for the new value
        self.counts2[new_val] += 1

    def count(self, tot: int) -> int:
        # Initialize the pair count to 0
        result = 0
        # For each unique value in nums1, compute the complement in nums2 that would sum to `tot`
        for value1 in self.counts1:
            complement = tot - value1
            # Add to the result the number of occurrences of the complement in nums2
            if complement in self.counts2:
                result += self.counts1[value1] * self.counts2[complement]
        return result