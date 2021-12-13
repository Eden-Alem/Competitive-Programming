import math
class Solution:
    def kClosest(self, points, k):
#         for i in range(1, len(points)):
#             val = points[i]
            
#             j = i - 1
#             while (j >= 0 and math.sqrt((val[0])**2 + (val[1])**2) < math.sqrt((points[j][0])**2 + (points[j][1])**2) ):
#                 points[j+1] = points[j]
#                 j -= 1
                
#             points[j+1] = val
            
#         return points[:k]


#         for i in range(len(points)):
#             minimum = i
#             for j in range(i+1, len(points)):
#                 if (math.sqrt((points[minimum][0])**2 + (points[minimum][1])**2) > math.sqrt((points[j][0])**2 + (points[j][1])**2)):
#                     minimum = j
                    
#             points[i], points[minimum] = points[minimum], points[i] 
            
#         return points[:k]
        
        return quickSort(0, len(points)-1, points)[:k]
    
def partitionPivot(first, last, array):      
    pivot_index = first 
    pivot = math.sqrt((array[pivot_index][0])**2 + (array[pivot_index][1])**2)

    while first < last:
        while first < len(array) and math.sqrt((array[first][0])**2 + (array[first][1])**2) <= pivot:
            first += 1

        while math.sqrt((array[last][0])**2 + (array[last][1])**2) > pivot:
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
    
    return array