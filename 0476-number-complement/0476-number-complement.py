class Solution:
    def findComplement(self, num: int) -> int:
        todo, bit = num, 1
        while todo:
            num ^= bit
            bit <<= 1
            todo >>= 1
        return num