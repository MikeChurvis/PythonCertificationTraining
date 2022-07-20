class QueueError(IndexError):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.__data = []

    def put(self, elem):
        self.__data.insert(0, elem)

    def get(self):
        if len(self.__data) == 0:
            raise QueueError('Queue is empty.')
        return self.__data.pop()


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
