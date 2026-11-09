class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 1
        count = 1
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            elif nums[i] != nums[i - 1]:
                count = 1
            res = max(res, count)

        return res * int(len(nums) > 0)
        