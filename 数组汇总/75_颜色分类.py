# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2, i = 0, len(nums)-1, 0
        while i <= p2:  # 注意，是 <=
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1  # 注意，因为是从左往右臊面，所以和p0交换来的，一定是1，所以可以不用再看，直接i+1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1 # p2则不一定，所以这了不能i + 1
            else:
                i += 1
