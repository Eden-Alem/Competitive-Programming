#User function Template for python3

class Solution:
    def __init__(self):
        self.arr = []
        # self.insert(8)
        # self.insert(6)
        # self.insert(4)
        # self.insert(11)
        # self.insert(8)
        # self.insert(9)
        # self.insert(10)
        # print(self.arr)
        # self.remove(0)
        # self.update(2, 10)
        # print(self.arr)
        print(self.buildHeap([5,7,6,1,12,3,13], 7))
        print(self.HeapSort([5,7,6,1,12,3,13], 7))
    #Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        # code here
        # parentI = self.parent(index)
        # while ((arr[parentI] > arr[index]) and index > 0):
        #     arr[parentI], arr[index] = arr[index], arr[parentI]
        #     index = parentI
         
        # rci = self.rightChild(index)
        # lci = self.leftChild(index)
        # while (index < n and lci < n and (arr[lci] < arr[index] or (rci < n and arr[rci] < arr[index]))):
        #     minI = rci if (rci < n and arr[lci] > arr[rci]) else lci
        #     arr[minI], arr[index] = arr[index], arr[minI]
        #     index = minI
        #     rci = self.rightChild(index)
        #     lci = self.leftChild(index)
        self.upHeap(arr, n, i)
        self.downHeap(arr, n, i)

    def upHeap(self, arr, n, index):
        parentI = self.parent(index)
        while (index > 0 and (arr[parentI] > arr[index])):
            arr[parentI], arr[index] = arr[index], arr[parentI]
            index = parentI
            parentI = self.parent(index)
    
    def downHeap(self, arr, n, index):
        minIndex = self.leftChild(index)
        
        if (minIndex >= n):
            return
        
        rci = self.rightChild(index)
        
        if (rci < n and arr[minIndex] > arr[rci]):
            minIndex = rci
            
        while (index < n and (arr[minIndex] < arr[index])):
            arr[minIndex], arr[index] = arr[index], arr[minIndex]
            index = minIndex
            self.downHeap(arr, n, index)

    
    #Function to build a Heap from array.
    def buildHeap(self, arr, n):
        # code here
        for node in range(n):
            self.upHeap(arr, n, node)
            # while (last > 0 and array[self.parent(last)] > array[last]):
            #     array[self.parent(last)], array[last] = array[last], array[self.parent(last)]
            #     last = self.parent(last) 
        # print(arr)       
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        while (n > 0):
            # self.buildHeap(arr, n)
            # arr[n-1]=self.getMin(arr)
            self.remove(arr, n, 0)
            # arr[0], arr[n-1] = arr[n-1], self.getMin(arr)
            n -= 1
            

        arr.reverse()
        print(arr)
    
    def getMin(self, arr):
        if(len(arr)):
            return arr[0]
        
    def leftChild(self, index):
        return (2 * index) + 1
    
    def rightChild(self, index):
        return (2 * index) + 2
    
    def parent(self, index):
        return (index - 1) // 2
        
    def insert(self, arr, n, value):
        # self.arr.append(element)
        # insertedI = len(self.arr) - 1
        # while ((self.arr[self.parent(insertedI)] > self.arr[insertedI]) and insertedI > 0):
        #     self.arr[self.parent(insertedI)], self.arr[insertedI] = self.arr[insertedI], self.arr[self.parent(insertedI)]
        #     insertedI = self.parent(insertedI)
        arr[n] = value
        self.upHeap(arr, n+1, n)

            
    def remove(self, arr, n, i):
        # lastI = len(self.arr) - 1
        # self.arr[lastI], self.arr[index] = self.arr[index], self.arr[lastI]
        # self.arr.pop()
        # lci = self.leftChild(index)
        # rci = self.rightChild(index)

        # while (index < len(self.arr) and lci < len(self.arr) and (self.arr[lci] < self.arr[index] or (rci < len(self.arr) and self.arr[rci] < self.arr[index]))):
        #     minI = rci if (rci < len(self.arr) and self.arr[lci] > self.arr[rci]) else lci
        #     self.arr[minI], self.arr[index] = self.arr[index], self.arr[minI]
        #     index = minI
        #     lci = self.leftChild(index)
        #     rci = self.rightChild(index)
        arr[n-1], arr[i] = arr[i], arr[n-1]
        self.heapify(arr, n-1, i)

            
    def update(self, arr, n, i, value):
        # if (index < len(self.arr)):
        #     self.arr[index] = element
        # parentI = self.parent(index)
        # while ((self.arr[parentI] > self.arr[index]) and index > 0):
        #     self.arr[parentI], self.arr[index] = self.arr[index], self.arr[parentI]
        #     index = parentI
         
        # rci = self.rightChild(index)
        # lci = self.leftChild(index)
        # while (index < len(self.arr) and lci < len(self.arr) and (self.arr[lci] < self.arr[index] or (rci < len(self.arr) and self.arr[rci] < self.arr[index]))):
        #     minI = rci if (rci < len(self.arr) and self.arr[lci] > self.arr[rci]) else lci
        #     self.arr[minI], self.arr[index] = self.arr[index], self.arr[minI]
        #     index = minI
        #     rci = self.rightChild(index)
        #     lci = self.leftChild(index)
        arr[i] = value
        self.heapify(arr, n, i)

    # def heapify(self, array):
    #     for last in range(len(array)-1,-1,-1):
    #         while (last > 0 and array[self.parent(last)] > array[last]):
    #             array[self.parent(last)], array[last] = array[last], array[self.parent(last)]
    #             last = self.parent(last)        
    #     return array

    # def heapSort(self, array):
    #     self.arr = []
    #     for element in array:
    #         self.insert(element)
        
    #     result = []
    #     while (len(self.arr)):
    #         result.append(self.getMin())
    #         self.remove(0)
    #     return result








a = Solution()


