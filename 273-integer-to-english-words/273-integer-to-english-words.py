class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        one_to_teen = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        def toWord(num):
            if num == 0:
                return ""
            
            if num <= 19:
                return one_to_teen[num-1]
            
            if num <= 99:
                return (tens[num//10 - 2] + " " + toWord(num%10)).rstrip()
            
            if num <= 999:
                return (toWord(num//100) + " Hundred " + toWord(num%100)).rstrip()
            
            if num <= 10**6-1:
                return (toWord(num//1000) + " Thousand " + toWord(num%1000)).rstrip()
            
            if num <= 10**9-1:
                return (toWord(num//(10**6)) + " Million " + toWord(num%(10**6))).rstrip()
            
            else:
                return (toWord(num//(10**9)) + " Billion " + toWord(num%(10**9))).rstrip()
            
        return toWord(num)
        
        
        
        
        
        