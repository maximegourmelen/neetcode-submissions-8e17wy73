class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i1 = None
        i2 = None
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums [i] + nums [j] == target:
                    i1 = i
                    i2 = j
        return [i1, i2]

        