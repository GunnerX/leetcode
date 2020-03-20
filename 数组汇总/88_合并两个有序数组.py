# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明:
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        双指针前序遍历法，需要O(n)空间复杂度
        """
        if not m:       # num1为空
            nums1[:] = nums2
            return None

        nums1_copy = nums1[:m]  # nums1要存储最终结果，所以遍历它的一个复制数组
        i,j,c= 0,0,0  # i,j分别遍历nums1_copy和nums2,c记录要在nums1中存储的位置

        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[c] = nums1_copy[i]
                i += 1
            else:
                nums1[c] = nums2[j]
                j += 1
            c += 1

        if i == m:
            nums1[c:] = nums2[j:]
        if j == n:
            nums1[c:] = nums1_copy[i:]


    def merge1(self, num1, m, num2, n):
        '''双指针后序遍历法,不需要额外空间'''
        i,j,c = m-1,n-1,m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[c] = nums2[j]
                j -= 1
            else:
                nums1[c] = nums1[i]
                i -= 1
            c -= 1
        nums1[:j + 1] = nums2[:j + 1]

s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m,n = 3,3
s.merge1(nums1, m, nums2, n)
print(nums1)



