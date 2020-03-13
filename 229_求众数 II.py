class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        major1, major2 = 0, 0
        count1, count2 = 0, 0
        res = []
        for num in nums:
            if num == major1:   count1 += 1 # 若投票给major1，则major1票数+1
            elif num == major2: count2 += 1 # 若投票给major2, 则major2票数+1
            elif not count1:    # 若当前没有无法删除的元素1，则更新major1,count1
                major1 = num
                count1 += 1
            elif not count2:    #  若当前没有无法删除的元素2，则更新major2,count2
                major2 = num
                count2 += 1
            else:   # 若当前元素及不等于major1也不等于major2，说明可以删除，则两者count1均减1
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for num in nums:    # 记录major1,2的个数，超过n/3则满足条件
            if num == major1:
                count1 += 1
            elif num ==major2:
                count2 += 1

        if count1 > n / 3:
            res.append(major1)
        if count2 > n / 3:
            res.append(major2)
        return res
