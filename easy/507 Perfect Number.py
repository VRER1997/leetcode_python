class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num == 6 or num == 28 or num == 496 or num == 8128 or num == 33550336


if __name__ == '__main__':
    s = Solution()
    s.checkPerfectNumber(28)