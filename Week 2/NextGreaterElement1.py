class Solution:
    def nextGreaterElement(self, nums1, nums2):
        remDict = {}
        monoStack = []        
        
        for i in range(len(nums2)):
            while(len(monoStack) and (nums2[i] > monoStack[-1])):
                remDict[monoStack.pop()] = nums2[i]                
                
            monoStack.append(nums2[i])
        
        for i in monoStack:
            remDict[i] = -1
            
        resultStack = []
        for num in nums1:
            resultStack.append(remDict[num])
        
        return resultStack