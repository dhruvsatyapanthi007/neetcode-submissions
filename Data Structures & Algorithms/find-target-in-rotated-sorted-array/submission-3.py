import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            res = bisect.bisect_left(nums, target, lo=0, hi=len(nums) - 1)
            if nums[res] == target:
                return res
            else:
                return -1

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid + 1

        if nums[-1] < target:
            res = bisect.bisect_left(nums, target, lo=0, hi=left - 1)
        else:
            res = bisect.bisect_left(nums, target, lo=left, hi=len(nums) - 1)

        return res if nums[res] == target else -1
        