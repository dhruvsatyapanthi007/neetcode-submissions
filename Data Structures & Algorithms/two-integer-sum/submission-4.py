class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val2Indices = collections.defaultdict(list)

        for i in range(0, len(nums)):
            val2Indices[nums[i]].append(i)

        for i in range(0, len(nums)):
            if nums[i] != target - nums[i]:
                if len(val2Indices[target - nums[i]]) != 0:
                    return [i, val2Indices[target - nums[i]][0]]
            else:
                if len(val2Indices[nums[i]]) == 2:
                    return val2Indices[nums[i]]
        