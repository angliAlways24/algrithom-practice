class Stack:
    def __init__(self, size):
        self.size=size
        self.array=[None]*self.size
        self.nextSlot=0

    def push(self, object):
        if not self.isFull():
            self.array[self.nextSlot]=object
            self.nextSlot+=1
    
    def pop(self):
        if not self.isEmpty():
            result=self.array[self.nextSlot-1]
            self.nextSlot-=1
            return result
        else:
            return None

    def isEmpty(self):
        return self.nextSlot==0

    def isFull(self):
        return self.nextSlot==self.size
