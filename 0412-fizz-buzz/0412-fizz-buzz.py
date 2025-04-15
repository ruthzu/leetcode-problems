class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        str_list=[]
        for num in range(1,n+1):
            if num%5!=0 and num%3!=0:
                str_list.append(str(num))
            elif num%5==0 and num%3==0:
                    str_list.append("FizzBuzz")    
            elif num%3==0:
                str_list.append("Fizz")
            elif num%5==0:
                str_list.append("Buzz")
        return str_list            


        