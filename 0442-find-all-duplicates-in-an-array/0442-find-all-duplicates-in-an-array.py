class Solution:
    def findDuplicates(self, nums):
        result = []

        # Iterate through each number in the array
        for num in nums:
            index = abs(num) - 1

            # Check if the value at this index has been negated (indicating a duplicate)
            if nums[index] < 0:
                result.append(index + 1)
            else:
                # Negate the value at this index to mark the number as seen
                nums[index] = -nums[index]

        return result