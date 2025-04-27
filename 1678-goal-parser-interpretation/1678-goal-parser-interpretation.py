class Solution:
    def interpret(self, command: str) -> str:
        r = []
        i = 0
        while i < len(command):
            if command[i] == "G":
                r.append("G")
                i += 1
            elif command[i] == "(" and command[i+1] == ")":
                r.append("o")
                i += 2
            elif command[i] == "(" and command[i+1:i+4] == "al)":
                r.append("al")
                i += 4
        return ''.join(r)
