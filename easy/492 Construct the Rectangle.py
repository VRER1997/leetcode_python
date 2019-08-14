from typing import List
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area ** 0.5), 0, -1):
            if area % i == 0:
                j = area / i
                return [max(i, j), min(i, j)]

if __name__ == '__main__':
    s = Solution()
    print(s.constructRectangle(4))