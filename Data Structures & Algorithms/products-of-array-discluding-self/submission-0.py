class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            f = nums[:i]
            b = nums[i + 1::]
            l = f + b
            output.append(self.product(l))

        return output

    def product(self, nums:List[int]) -> int:
        to_ret = 1
        for num in nums:
            to_ret = to_ret * num

        return to_ret


        