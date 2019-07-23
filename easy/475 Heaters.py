from typing import List
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def check(r):
            i, j = 0, 0
            while i < len(houses) and j < len(heaters):
                if heaters[j] - r <= houses[i] <= heaters[j] + r:
                    i += 1
                elif houses[i] < heaters[j] - r:
                    return False
                else:
                    j += 1
            return i == len(houses)

        l, r = 0, max(houses[-1], heaters[-1]) + 1
        while l <= r:
            mid = (l+r) // 2
            #print(l, " ", r, " ", mid)
            if check(mid):
                r = mid-1
            else:
                l = mid+1
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.findRadius([1,2,3,5,15],
[2,30]))
