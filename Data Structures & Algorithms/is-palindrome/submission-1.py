class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = re.sub(r"[^a-zA-z0-9]", "", s).lower()
        str2 = str1[::-1]

        if str1 == str2:
            return True
            

        return False