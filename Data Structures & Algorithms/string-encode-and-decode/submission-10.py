class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += '#'+ str(len(strs[i])) + "#" + strs[i]
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while(i < len(s)):
            num = ""
            n = i + 1
            while(s[n] != '#'):
                num += s[n]
                n += 1
            l = int(num)
            i = n + 1
            curStr = ""
            j = i
            while(l > 0):
                j += 1
                l -= 1
            res.append(s[i:j])
            print(res)
            i = j
        return res


                
                



