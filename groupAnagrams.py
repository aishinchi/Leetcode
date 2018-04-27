class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        count = 1
        falg = 0
        out = [[strs[0]]]
        lens = len(strs)
        for i in range(lens):
            for j in range(count):
                if (self.compare(out[j][0], strs[i])):
                    out[j].append(strs[i])
                    flag = 1
                    break
            if flag == 0:
                out.append([strs[i]])
                count += 1
            elif flag == 1:
                flag = 0
        out[0].pop(0)
        return out

    def dictionary(self):
        dic = {}
        for i in range(97, 123):
            dic[chr(i)] = 0
        return dic

    def compare(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        if len1 != len2:
            return False
        else:
            dic = self.dictionary()
            for i in range(len1):
                dic[str1[i]] += 1
                dic[str2[i]] -= 1
            for item in dic:
                if dic[item] != 0:
                    return False
            return True

a = Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))