import math
import heapq

def kClosest(self, points, k):
    minHeap = []
    for x, y in points: 
        dist = (x ** 2) + (y ** 2)
        minHeap.append([dist, x, y])
    heapq.heapify(minHeap)

    res = []
    i = 0
    while i < k: 
        dist, x, y = heapq.heappop(minHeap)
        res.append([x, y])
        i += 1
    return res