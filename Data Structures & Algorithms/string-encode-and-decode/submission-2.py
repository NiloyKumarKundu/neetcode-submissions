class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        string = ""
        for word in strs:
            string += word
            string += "é"

        return string

    def decode(self, s: str) -> List[str]:
        strs = []

        flag = ""

        for i in s:
            if i != "" and i != "é":
                flag += i
            if i == "é":
                strs.append(flag)
                flag = ""
        return strs
        
            
            
