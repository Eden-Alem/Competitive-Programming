class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        arr = []
        for i in range(len(l)):
            temp = sorted(nums[l[i]:r[i]+1])
            arr.append(isArthSequence(temp))
            
        return arr    

def isArthSequence(arr):
    difference = arr[1] - arr[0]
    for i in range(len(arr) - 1):
        if (arr[i+1] - arr[i] != difference): return False 
        
    return True