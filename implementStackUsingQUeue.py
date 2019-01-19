class Stack:

    def __init__(self, queue):
        self.queue=queue

    def push(self, obj):
        self.queue.append(obj)

    def pop(self):
        result = self.__getTail()
        return result

    def peek(self):
        result = self.__getTail()
        self.queue.push(result)
        return result

    def __getTail(self):
        size=len(self.queue)
        for i in xrange(size-1):
            tmp=self.queue.pop()
            self.queue.push(tmp)
        result=self.queue.pop()
        return result

        