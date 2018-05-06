import time
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lens = len(nums)
        if lens==0:
            return [[]]
        nums.sort()
        out = []
        # self.permuteUniqueCore(nums, 0, lens,out)
        self.permuteUniqueCore(nums, [], out)
        return out
    #my way 主要是去重耗时太大
    # def permuteUniqueCore(self, nums, begin, lens, out):
    #     if begin == lens-1:
    #         tmp = nums[:]
    #         if tmp not in out:
    #             out.append(tmp)
    #     else:
    #         for i in range(begin,lens):
    #             if nums[i] == nums[begin] and i!= begin:
    #                 continue
    #             else:
    #                 temp = nums[begin]
    #                 nums[begin] = nums[i]
    #                 nums[i] = temp
    #                 self.permuteUniqueCore(nums, begin+1, lens, out)
    #                 temp = nums[begin]
    #                 nums[begin] = nums[i]
    #                 nums[i] = temp

    #leetcode 的方法重写
    def permuteUniqueCore(self, nums, curr, out):
        if len(nums) == 0:
            out.append(curr)
        else:
            for i in range(len(nums)):
                if i >0 and nums[i] == nums[i-1]:
                    continue
                else:
                    self.permuteUniqueCore(nums[0:i]+nums[i+1:], curr+[nums[i]], out)

start = time.time()
a = Solution()
b = a.permuteUnique([2,2,1])
end = time.time()
spendtime = end - start
print(spendtime)
print(b)
print(len(b))