import math
import heapq

def kClosest(points, k):
    minHeap = []
    for i in range(len(points)):
        point1 = abs((points[i][0] - 0) ** 2)
        point2 = abs((points[i][1] - 0) ** 2)
        distance = math.sqrt(point1 + point2)
        minHeap.append([distance, points[i][0], points[i][1]])
    
    heapq.heapify(minHeap)
    result = []
    for i in range(k):
        result.append([minHeap[0][1], minHeap[0][2]])
        heapq.heappop(minHeap)
    return result