# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret = []
        for i in sorted(intervals, key=lambda x: x.start):
            if ret and i.start <= ret[-1].end:
                ret[-1].end = max(ret[-1].end, i.end)
            else:
                ret.append(i)
        return ret
