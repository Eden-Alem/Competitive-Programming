class Solution:
    def bestClosingTime(self, customers: str) -> int:
        shops = []
        
        for c in customers:
            if c == 'Y':
                shops.append(1)
            else:
                shops.append(-1)
                
        prefix = [0]
        
        for i in range(len(shops)):
            prefix.append((prefix[-1] + shops[i]))
            
        return prefix.index(max(prefix))
        
        