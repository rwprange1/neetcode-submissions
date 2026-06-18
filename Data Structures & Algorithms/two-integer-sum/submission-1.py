class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        eles = {value: index for index, value in enumerate(nums)}
        
        for i in range(len(nums)):
            if target - nums[i] in eles and i is not eles[target - nums[i]] :
                return [i, eles[target - nums[i]]]

        
