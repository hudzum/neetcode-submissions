class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        one = 0
        two = len(s)-1
        
        
        while one < two:
            if not s[one].isalnum():
                one+=1
                continue

            if not s[two].isalnum():
                two-=1
                continue

            if s[one].lower() != s[two].lower():
                return False
            
            one+=1
            two-=1
        
        return True


        
  

           