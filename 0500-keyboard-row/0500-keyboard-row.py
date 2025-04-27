class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r=[]
        first= set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        for i in words:
            if set(i.lower()) <= first:
                r.append(i)
            elif set(i.lower()) <= second:
                r.append(i)
            elif set(i.lower()) <= third:
                r.append(i)
            else:
                continue        
        return r

