class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
        