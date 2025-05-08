class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for st, en, di in shifts:
            k = 1 if di == 1 else -1
            diff[st] += k
            diff[en + 1] -= k

        ans = []
        running = 0
        for i, ch in enumerate(s):
            running = (running + diff[i]) % 26
            ordered = (ord(ch) - ord('a') + running) % 26 + ord('a')
            ans.append(chr(ordered))

        return "".join(ans)
