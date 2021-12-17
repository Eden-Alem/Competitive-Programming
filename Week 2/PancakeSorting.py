class Solution:
    def pancakeSort(self, arr):
        right = len(arr) - 1
        
        isSorted = True
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                isSorted = False
                break
        if isSorted: return []
        
        res = []
        temp = arr[:right+1]
        
        while (right):
            maxValIndex = max_index(temp)
            
            leftArray = temp[:maxValIndex+1]
            if not maxValIndex == right:
                rightArray = temp[maxValIndex+1:]
                leftArray.reverse()
                
                res.append(maxValIndex+1)
                leftArray.extend(rightArray)
                leftArray.reverse()
                
                res.append(right+1)
                
            temp = leftArray[:right]
            
            right -= 1
            
        return res
    

def max_index(arr):
    max_i = 0
    for i in range(len(arr)):
        if (arr[i] > arr[max_i]):
            max_i = i

    return max_i