class Solution:
    def kthLargestNumber(self, nums, k: int):
        # nums.sort(key=lambda x: int(x))
        # return nums[-k]
        
        mergeSort(nums)
        return nums[-k]
        
def merge(left, right, array):
    i, j, k = 0, 0, 0
    
    while (i < len(left) and j < len(right)):
        if (int(left[i]) <= int(right[j])):
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    while(i < len(left)):
        array[k] = left[i]
        i += 1
        k += 1
    
    while(j < len(right)):
        array[k] = right[j]
        j += 1
        k += 1
    
    return array


def mergeSort(array):
    if (len(array) < 2):  return
    
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    
    mergeSort(left)
    mergeSort(right)
    
    merge(left, right, array)