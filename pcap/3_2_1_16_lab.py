class QueueError(IndexError):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self._data = []

    def put(self, elem):
        self._data.insert(0, elem)

    def get(self):
        if len(self._data) == 0:
            raise QueueError('Queue is empty.')
        return self._data.pop()


class SuperQueue(Queue):    
    def isempty(self):
        return len(self._data) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
