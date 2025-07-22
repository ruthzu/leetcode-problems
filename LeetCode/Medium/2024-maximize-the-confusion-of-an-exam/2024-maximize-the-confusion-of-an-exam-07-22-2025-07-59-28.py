class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        def answer(target):
            left=0
            flip=0
            maxi=0
            for i in range(len(answerKey)):
                if answerKey[i]==target:
                    flip+=1
                if k<flip:
                    if answerKey[left]==target:
                        flip-=1
                    left+=1
            maxi=max(maxi,i-left+1)
            return(maxi)
        return max(answer('T'),answer('F'))  

        