import heapq

a = [3, 4, 5, 7, 8]
heapq.heapify(a)
print(a)

heapq.heappop(a)
print(a)

heapq.heappush(a, 4)
print(a)

