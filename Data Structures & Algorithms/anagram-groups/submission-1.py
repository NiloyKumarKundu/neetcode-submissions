class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        flag = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key in flag:
                flag[key].append(word)
            else:
                flag[key] = [word]
        
        return list(flag.values())
         