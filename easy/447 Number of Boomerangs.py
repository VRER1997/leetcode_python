from typing import List
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        def dist(a, b):
            return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])
        res = 0
        n = len(points)
        for i in range(n):
            dit = {}
            for j in range(n):
                distance = dist(points[i], points[j])
                if distance not in dit:
                    dit[distance] = 1
                else:
                    dit[distance] += 1
            for val in dit.values():
                res += (val * (val-1))

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfBoomerangs([[0,0],[1,0],[2,0]]))

