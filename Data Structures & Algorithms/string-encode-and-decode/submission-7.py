class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += '#'+ "new" + strs[i]
        return res
    def decode(self, s: str) -> List[str]:
        return s.split("#new")[1:]
                
                



