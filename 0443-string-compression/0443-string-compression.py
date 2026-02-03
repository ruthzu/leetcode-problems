class Solution:
    def compress(self, chars: List[str]) -> int:

        N = len(chars)
        writer = 0
        reader = 0

        while reader < N:
            current = chars[reader]
            count = 0


            while reader < N and chars[reader] == current:
                reader += 1
                count += 1

            chars[writer] = current
            writer += 1

            if count > 1:
                for digits in str(count):
                    chars[writer] = digits
                    writer += 1
                   
        return writer 
