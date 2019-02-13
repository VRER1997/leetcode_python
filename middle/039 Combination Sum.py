class Solution:
    ret = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(remain, combi, idx):
            #失败条件是 candidates为空或target为负或idx >= len(cadidates)
            if remain < 0: return
            if remain == 0:
                res.append(combi)
                return
            if idx >= len(candidates): return
            # 选 或者 不选
            dfs(remain, combi, idx+1)
            dfs(remain-candidates[idx], combi+[candidates[idx]], idx)
        

        res = []
        dfs(target, [], 0)
        return res
