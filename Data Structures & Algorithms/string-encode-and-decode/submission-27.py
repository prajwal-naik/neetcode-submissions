class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += "#" + str(len(strs[i])) + "#" + strs[i]
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            if(s[i] == "#"):
                count = ""
                i += 1
                while(s[i] != "#"):
                    count += s[i]
                    i += 1
                i += 1
                count = int(count)
                curStr = ""
                while(count != 0):
                    curStr += s[i]
                    i += 1
                    count -= 1
                res.append(curStr)
        return res