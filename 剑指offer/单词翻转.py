class Solution:
    def reverseWords(self, s: str) -> str:

        def make_list(s):  # 去掉多余空格并转化为列表
            l, r, s_list = 0, len(s) - 1, []
            while l <= r and s[l] == ' ':  # 去掉前后的空格
                l += 1
            while l <= r and s[r] == ' ':
                r -= 1
            while l <= r:  # 字符串转化为列表并去掉中间多余的空格
                if s[l] != ' ':
                    s_list.append(s[l])
                elif s_list[-1] != ' ':  # 注意这里，能去掉中间多余的空格
                    s_list.append(s[l])
                l += 1
            return s_list

        def reverse(s, l, r):  # 反转函数
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        s_list = make_list(s)  # 去掉多余空格并转化为列表
        l, r = 0, 0
        reverse(s_list, 0, len(s_list) - 1)  # 反转整个句子
        while r < len(s_list):  # 再反转每个单词
            if s_list[r] == ' ':
                reverse(s_list, l, r - 1)
                l = r + 1
            r += 1
        reverse(s_list, l, len(s_list) - 1)  # 反转最后一个单词
        return ''.join(s_list)