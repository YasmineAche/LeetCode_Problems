class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, num in enumerate(nums):
            nums[index]= ""
            for i, _ in enumerate(nums[index+1:]):
                if num + _ == target :
                    return [index, nums.index(_)]
            