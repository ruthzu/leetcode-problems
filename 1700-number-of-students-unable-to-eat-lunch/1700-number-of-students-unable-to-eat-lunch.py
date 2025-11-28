class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import Counter
        cnt = Counter(students)
        
        for s in sandwiches:
            if cnt[s] == 0:
                break
            cnt[s] -= 1
        
        return cnt[0] + cnt[1]
