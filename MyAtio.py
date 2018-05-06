class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        lens = len(str)
        if lens == 0:
            return 0
        flag = 1
        numStr = ""
        if '0' <= str[0] <= '9':
            numStr += str[0]
        if str[0] < '0' or str[0] >'9':
            if str[0] == '-':
                flag = -1
            elif str[0] == '+':
                flag = 1
            else:
                return 0
        for i in range(1, lens):
            if '0' <= str[i] <= '9':
                numStr += str[i]
            else:
                break
        numStr = numStr.lstrip('0')
        numLen = len(numStr)
        if numLen == 0:
            return 0
        elif numLen > 10:
            pass
        else:
            num = int(numStr)
            if num > 2147483647:
                pass
            else:
                return flag*num
        if flag == -1:
            return -2147483648
        else:
            return 2147483647


a = Solution()
b = a.myAtoi("  -0000000000024154354312345678")
print(b)