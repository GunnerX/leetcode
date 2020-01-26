# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


def threeSum(nums):
    n = len(nums)
    if n < 3:
        return []
    nums.sort()
    res = []
    for k in range(n - 2):  # 遍历排序后数组
        if nums[k] > 0:     # 若 nums[k]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
            break
        if k > 0 and nums[k] == nums[k - 1]:  # 对于重复元素直接跳过，避免出现重复解
            continue
        i, j = k + 1, n - 1   # 左右指针
        while i < j:
            sums = nums[i] + nums[j] + nums[k]

            if sums == 0:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]: # 判断左界和右界是否和下一位置重复，去除重复解
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1

            elif sums < 0:  # 若和小于 0，说明 nums[i] 太小，i 右移
                i += 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1

            else:   # 若和大于 0，说明 nums[j] 太大，j 左移
                j -= 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
    return res
