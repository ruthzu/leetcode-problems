class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        a = sorted(c.keys(), key=lambda x: -c[x])
        r = []
        for ch in a:
            r.append(ch * c[ch])
        return "".join(r)
