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
        dic = {}
        for i in range(lens):
            if nums[i] in dic.values():
                return [nums.index(target - nums[i]), i]
            else:
                dic[nums[i]] = target - nums[i]
                