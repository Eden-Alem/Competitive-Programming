class Solution:
    def largestNumber(self, nums):
        return str(int(quickSort(0,len(nums)-1, nums)))
        

def partitionPivot(first, last, array):      
    pivot_index = first 
    pivot = str(array[pivot_index])

    while first < last:
        while first < len(array) and ((str(array[first]) + pivot) >= (pivot + str(array[first]))):
            first += 1

        while (str(array[last]) + pivot) < (pivot + str(array[last])):
            last -= 1

        if(first < last):
            array[first], array[last] = array[last], array[first]

    array[last], array[pivot_index] = array[pivot_index], array[last]

    return last
      
def quickSort(left, right, array):
      
    if (left < right):          
        p = partitionPivot(left, right, array)
          
        quickSort(left, p - 1, array)
        quickSort(p + 1, right, array)
    
    return ''.join(str(a) for a in array)
                                            