class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        nums.sort()

        for i in range(0, len(nums) - 2):
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                pairSum = nums[j] + nums[k]

                if pairSum > target:
                    k -= 1
                elif pairSum < target:
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        return list(list(triplet) for triplet in res)
