class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
             return 0

        sort = sorted(nums)
        print(sort)

        to_ret = 1
        current = 1
        for i in range(1, len(nums)):
            diff = sort[i] - sort[i-1]
            if diff == 1:
                current += 1
            elif  diff != 0:
                to_ret = to_ret if to_ret >= current else current
                current = 1

        return to_ret if to_ret >= current else current