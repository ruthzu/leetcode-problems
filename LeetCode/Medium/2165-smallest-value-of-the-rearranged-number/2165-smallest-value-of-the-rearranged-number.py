class Solution:
    def smallestNumber(self, num: int) -> int:
        nums=list(str(num))
        if nums[0]=='-':
            sort_num=sorted(nums[1:],reverse=True)
            return int('-'+''.join(sort_num))
        else:
            sort_num=sorted(nums)
            if sort_num[0]=='0':
                for i in range(1,len(sort_num)):
                    if sort_num[i]!='0':
                        sort_num[0],sort_num[i]=sort_num[i],sort_num[0]
                        break
            return int(''.join(sort_num)) 
