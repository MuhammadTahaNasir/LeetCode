class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        return max([num for num, freq in count.items() if num == freq], default=-1)
