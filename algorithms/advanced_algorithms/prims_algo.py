import heapq

# initialize an empty list
minHeap = list()

heapq.heappush(minHeap, (0, 1))

heapq.heappush(minHeap, (-1, 5))

heapq.heappush(minHeap, (2, 0))

heapq.heappush(minHeap, (5, -1))

print("After pushing, now heap looks like: {}".format(minHeap))


# pop and return smallest element from the heap
smallest = heapq.heappop(minHeap)

print("Smallest element in the original list was: {}".format(smallest))

print("After popping, heap looks like: {}".format(minHeap))
