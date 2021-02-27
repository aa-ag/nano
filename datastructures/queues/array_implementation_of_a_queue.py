###--- CREATE QUEUE ---###
class Queue:

    def __init__(self, default_size=10):
        self.arr = [0 for _ in range(default_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0


###--- TESTING __init__ ---###
q = Queue()
print(q.arr)
print("Pass" if q.arr == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] else "Fail")
