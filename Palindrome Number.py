class Solution:
    def isPalindrome(self, x: int) -> bool:
         num = str(x)
         mylist = []
         i = 0
         while i < len(num):
            mylist.append(num[i])
            i += 1
         mylist2 = mylist.copy()
         mylist2.reverse()
         j = 0
         ans = True
         for number in mylist2:
            if number == mylist[j]:
                j += 1
            else:
                ans = False
                break
         return ans
        
