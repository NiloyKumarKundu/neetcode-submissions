class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        flag = {}

        for i in range(len(s)):
            flag[s[i]] = flag.get(s[i], 0) + 1

        for i in range(len(t)):
            if flag.get(t[i], 0) == 0:
                return False
            flag[t[i]] -= 1
            
        return True


        