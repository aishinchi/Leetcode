import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 新建一个默认字典，键值为list类型
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())


a = Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))