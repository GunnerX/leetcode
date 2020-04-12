# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
#
#  
#
# 示例 1:
#
# 输入: [1,2,3,4,5]
# 输出: True
#  
#
# 示例 2:
#
# 输入: [0,0,1,2,5]
# 输出: True
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def isStraight(self, nums):
        '''连续的几个不重复数字，其中最大值max，最小值min，则数字个数为max - min + 1
            由此可知，要使5张牌连续，则要使max - min + 1 <= 5
            1. max - min + 1 > 5    此情况下即使有大小王两张牌也不足以使5张牌连续
            2. max - min + 1 = 5    此情况下不含大小王5张牌已连续
            3. max - min + 1 < 5    此情况下5张牌中含大小王，补上后可使其连续'''


        min_ = 14
        max_ = 0
        dct = {}    # 记录有无重复元素出现
        for num in nums:
            if num == 0:    # 遇到大小王则跳过
                continue
            if num in dct:  # 存在重复元素则不符合条件
                return False
            dct[num] = 1    # 记录已经出现过的元素
            min_ = min(min_, num)   # 更新最小值
            max_ = max(max_, num)   # 更新最大值
        return max_ - min_ + 1 <= 5
