class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack=[]
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i in mapping.keys() :
                if not stack:
                    return False
                else:
                    j= stack.pop()
                    if j!=mapping[i]:
                        return False
        return not stack        
    