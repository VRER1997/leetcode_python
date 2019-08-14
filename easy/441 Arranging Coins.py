class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, 2**31+1
        while l <= r:
            mid = l + (r-l) // 2
            d = (mid*(mid+1))/2
            if d == n: return mid
            elif d < n: l = mid+1
            else: r = mid-1

        return r

if __name__ == '__main__':
    s = Solution()
    print(s.arrangeCoins(8))