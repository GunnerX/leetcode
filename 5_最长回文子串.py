# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def judge(self, s):
        '''判断一个字符串是否回文'''
        size = len(s)
        i,j = 0,size-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        p = 0
        q = 0
        for i in range(size-1):
            for j in range(i+1, size):
                if Solution.judge(self, s[i:j+1]) and j-i > q-p:
                    p,q = i,j
        return s[p:q+1]

s = ''
solution = Solution()
print(solution.longestPalindrome(s))
