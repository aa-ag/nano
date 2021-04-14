import heapq

# initialize an empty list
minHeap = list()

# insert 5 into heap
heapq.heappush(minHeap, 6)

# insert 6 into heap
heapq.heappush(minHeap, 6)

# insert 2 into heap
heapq.heappush(minHeap, 2)

# insert 1 into heap
heapq.heappush(minHeap, 1)

# insert 9 into heap
heapq.heappush(minHeap, 9)

print("After pushing, heap looks like: {}".format(minHeap))


# pop and return smallest element from the heap
smallest = heapq.heappop(minHeap)

print("Smallest element in the original list was: {}".format(smallest))

print("After popping, heap looks like: {}".format(minHeap))
