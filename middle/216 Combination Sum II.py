from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []
        def dfs(k, n, res: List):
            if k == 0:
                if n == 0:
                    #print(res)
                    result.append(res[:])
                return

            for i in range(1, 10):
                if i > n: continue
                if res.count(i): continue
                if len(res) > 0 and i < res[-1]: continue
                res.append(i)
                dfs(k - 1, n - i, res)
                res.remove(i)

        dfs(k, n, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 9))