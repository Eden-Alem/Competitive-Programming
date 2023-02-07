class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        result = []
        while len(freq):
            temp_res = [None] * (n+1)
            temp_dict = dict(freq.most_common(n+1))
            
            j = 0
            for i in temp_dict:
                temp_res[j] = i
                freq[i] -= 1
                j += 1
                if (freq[i] == 0):
                    del freq[i]
                    
            result.extend(temp_res)
            
        while result and result[-1] == None:
            del result[-1]
            
        return len(result)
        