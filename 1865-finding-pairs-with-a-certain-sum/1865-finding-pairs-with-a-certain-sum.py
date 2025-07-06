class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # Initialize nums1, nums2, and create a counter for nums2 to track frequency of elements
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts = Counter(nums2)  # This keeps track of how many times each value appears in nums2

    def add(self, index: int, val: int) -> None:
        # Update nums2 at the specified index and adjust the counts accordingly
        old_val = self.nums2[index]
        # Remove the old value from the counter (decrement count)
        self.counts[old_val] -= 1
        # If the count reaches zero, remove the entry for that value to keep the counter clean
        if self.counts[old_val] == 0:
            del self.counts[old_val]
        
        # Update the value in nums2
        self.nums2[index] += val
        new_val = self.nums2[index]
        # Increment the counter for the new value
        self.counts[new_val] += 1

    def count(self, tot: int) -> int:
        # For each value in nums1, calculate how many times (tot - value) appears in nums2
        result = 0
        for value in self.nums1:
            result += self.counts[tot - value]
        return result
