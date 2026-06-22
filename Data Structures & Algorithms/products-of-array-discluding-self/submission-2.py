class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product  = 1 
        zeros = 0

        for num in nums:
            if num != 0:
                product *= num
            else:
                zeros += 1

        if zeros >= 2:
            return [0] * len(nums)


        to_ret = [0] * len(nums)
        for i in range(len(nums)):
            if zeros:
                to_ret[i] = 0 if nums[i] != 0 else product
            else:
                to_ret[i] = product // nums[i]

        return to_ret            





        