class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 有一个点的最大跳跃距离nums[i] == 0
        # 且我们不能跳得比这个点更远的时候，我们才无法到达最后

        '''
        if len(nums) == 1: return True
        for i in range(len(nums)-1):
            if nums[i] == 0:
                flag = False
                for j in range(i):
                    if j+nums[j] > i:
                        flag = True
                if not flag:
                    return False
        return True
        '''

        # 我们可以从头到尾遍历，始终维护一个当前能跳的最大长度max_jump，
        #
        # 一旦max_jump小于等于0了，说明我们无法走的更远了，立刻返回False
        # 一旦max_jump + 当前index >= last index了，立刻返回True

        if len(nums) == 1: return True
        max_jump = 0
        for i in range(len(nums)):
            # 向前走一步，要么消耗一步最大步长，要么借用下一步的步长
            max_jump = max(max_jump-1, nums[i])
            if max_jump + i >= len(nums)-1:
                return True
            if max_jump < 0:
                return False


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4]))