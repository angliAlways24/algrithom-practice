class MinStack:
    def __init__(self):
        self.stack=Stack(30)
        self.minStack=Stack(30)

    def push(self, obj):
        self.stack.push(obj)
        if self.minStack.isEmpty(): 
            self.minStack.push(obj)
        elif obj<=self.minStack.peek():
            self.minStack.push(obj)
        
    def pop(self):
        if self.stack.peek()==self.minStack.peek():
            self.minStack.pop()
        return self.stack.pop()

    def getMin(self):
        if self.minStack.isEmpty():
            return None
        else :
            self.minStack.peek()



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

    def peek(self):
        pass

    def isEmpty(self):
        return self.nextSlot==0

    def isFull(self):
        return self.nextSlot==self.size

