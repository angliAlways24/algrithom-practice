class Queue:
    def __init__(self, size):
        self.array=[None]*size
        self.size=size
        self.nextSlot=0
        
    def push(self, object):
        if self.isNotFull():
            self.array[self.nextSlot]=object
            self.nextSlot+=1
        else:
            return
    
    def pop(self):
        result = None
        if self.isNotEmpty():
            result=self.array[0]
            firstPopped=1
            while firstPopped<self.nextSlot:
                self.array[firstPopped-1]=self.array[firstPopped]
                firstPopped+=1
            self.nextSlot-=1
        return result

    def isNotFull(self):
        return self.array[self.size-1]==None

    def isNotEmpty(self):
        return self.nextSlot>0
        