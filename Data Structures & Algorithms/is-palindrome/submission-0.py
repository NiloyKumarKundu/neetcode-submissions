class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        i = 0
        j = len(strs) - 1

        while (i < j):
            if strs[i] != strs[j]:
                return False
            i += 1
            j -= 1
            

        return True