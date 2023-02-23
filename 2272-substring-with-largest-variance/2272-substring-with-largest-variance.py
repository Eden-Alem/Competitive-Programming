class Solution:
    def largestVariance(self, s: str) -> int:
        chars = Counter(s)
        
        result = 0
        for char1, char2 in itertools.permutations(chars, 2):
            visit_char1 = False
            visit_char2 = False
            
            variance = 0
            count_char1 = chars[char1]
            count_char2 = chars[char2]
            
            for char in s:
                if char not in (char1, char2):
                    continue
                    
                if variance < 0:
                    if not count_char1:
                        break
                        
                    if not count_char2:
                        result = max(result, variance + count_char1)
                        break
                        
                    visit_char1 = visit_char2 = False
                    variance = 0
                        
                if char == char1:
                    count_char1 -= 1
                    variance += 1
                    visit_char1 = True
                    
                if char == char2:
                    count_char2 -= 1
                    variance -= 1
                    visit_char2 = True
                    
                if visit_char1 and visit_char2:
                    result = max(result, variance)
                    
        return result
                            
                            
                            
                            
        