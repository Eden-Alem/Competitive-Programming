class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        elif num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        
        if (len(self.maxHeap) - len(self.minHeap) >= 2):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif (len(self.minHeap) - len(self.maxHeap) >= 2):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if (len(self.minHeap) == len(self.maxHeap)):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        else:
            if (len(self.minHeap) > len(self.maxHeap)):
                return float(self.minHeap[0])
    
            else:
                return -float(self.maxHeap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()