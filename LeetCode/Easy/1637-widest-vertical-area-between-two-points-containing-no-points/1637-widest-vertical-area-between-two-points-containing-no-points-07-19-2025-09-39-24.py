class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        arr=[]
        for i in range(len(points)):
            arr.append(points[i][0])
        arr.sort()
        j=0
        for i in range(0,len(arr)-1):
            if arr[i+1]-arr[i]>j:
                j=arr[i+1]-arr[i] 
        return j           
        