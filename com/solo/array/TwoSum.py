from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictry = {};

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict.keys():
                return [i, dict[diff]]
            else:
                dictry[nums[i]] = i
        return []
