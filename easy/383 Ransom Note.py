import re
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for char in ransomNote:
            ret_str, num = re.subn(char,'',magazine,count=1)
            magazine = ret_str
            if not num: return False
        return True