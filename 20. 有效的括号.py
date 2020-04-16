# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def isValid(self, s):
        dct = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            # 如果是开括号则入栈
            if char in dct:
                stack.append(char)
            # 如果是闭括号
            else:
                # 栈非空则从栈中弹出栈顶元素否则不匹配
                if stack:
                    top = stack.pop()
                else:
                    return False
                # 如果弹出的括号不匹配
                if dct[top] != char:
                    return False
        return not stack













