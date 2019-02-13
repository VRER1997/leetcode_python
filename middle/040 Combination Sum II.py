class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(target, combi, idx):
            if target < 0 : return
            if target == 0 and combi not in res:
                res.append(combi)
                return
            if idx >= len(candidates): return
            dfs(target, combi, idx+1)
            dfs(target-candidates[idx], combi+[candidates[idx]], idx+1)

        res = []
        candidates.sort()
        dfs(target, [], 0)
        return res
