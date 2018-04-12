class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        lens = len(nums)
        for i in range(lens-1):
            for j in range(i+1, lens):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i,j]