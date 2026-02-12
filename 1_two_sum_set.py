class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for index, item in enumerate(nums):
            complemento = target - item
            if complemento in seen:
                return [seen.get(complemento), index]
            seen[item] = index
        return False
