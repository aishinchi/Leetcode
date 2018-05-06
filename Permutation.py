class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        out = []
        lens = len(nums)
        self.permutation(nums, 0, lens, out)
        return out

    def permutation(self, nums, begin, lens, out):
        if (begin==lens-1):
            temp = nums[:]
            out.append(temp)
        else:
            for i in range(begin,lens):
                tmp = nums[begin]
                nums[begin] = nums[i]
                nums[i] = tmp
                self.permutation(nums, begin+1, lens, out)
                tmp = nums[begin]
                nums[begin] = nums[i]
                nums[i] = tmp

a =Solution()
out = a.permute([1,2,3])
print(out)



