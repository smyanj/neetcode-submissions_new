class Solution:

    def encode(self, strs: List[str]) -> str:
        empty = ""
        for w in strs:
            empty += w + " "

        print(empty)
        return empty

    def decode(self, s: str) -> List[str]:
        streak = ""
        res = []
        for w in s:
            if w != " ":
                streak += w
            else:
                res.append(streak)
                streak = ""
        
        return res