class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt_even = cnt_odd = 0         # counts for all-even / all-odd subsequences
        alt_even = alt_odd = 0         # alternating subseqs: one starting with even, one with odd

        for num in nums:
            if num % 2 == 0:
                cnt_even += 1
                alt_even = alt_odd + 1
            else:
                cnt_odd += 1
                alt_odd = alt_even + 1

        return max(cnt_even, cnt_odd, alt_even, alt_odd)