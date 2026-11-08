class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        leftProduct = [1]
        rightProduct = [1]

        for i in range(0, len(nums) - 1):
            leftProduct.append(leftProduct[-1] * nums[i])
            rightProduct.append(rightProduct[-1] * nums[-i - 1])

        rightProduct = rightProduct[::-1]

        for i in range(0, len(nums)):
            nums[i] = leftProduct[i] * rightProduct[i]
        return nums
        