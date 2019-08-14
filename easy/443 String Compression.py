class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if chars == []: return chars
        chars.append('~')
        l, cnt, offset = chars[0], 0, 0
        for index, ch in enumerate(chars):
            if ch == l:
                cnt += 1
            else:
                if cnt == 1:
                    chars[index-offset-1] = l
                if cnt >= 2:
                    offset += (cnt-2)
                    chars[index-offset-2] = l
                if cnt > 1 and cnt < 10:
                    chars[index-offset-1] = str(cnt)
                if cnt >= 10:
                    i = 0
                    while i < len(str(cnt)):
                        chars[index - offset - 1 + i] = str(cnt)[i]
                        i += 1
                    offset -= (len(str(cnt))-1)
                l, cnt = chars[index], 1
        chars.pop()
        #print(chars)
        #print(offset)
        return len(chars)-offset

if __name__ == '__main__':
    s = Solution()
    print(s.compress(["$","$","$","#","#","#","#","#","$","$"]))