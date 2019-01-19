class Student:

    def getHashCode(self):
        return ""

class HashSet:

    def __init__(self, size):
        self.array = [None] *size

    def add(self, obj):
        if obj is None:
            return

        jointSlot = self.__findPosition(obj)
        jointSlot.append(obj)

    def __findPosition(self, obj):
        hashCode = obj.getHashCode()
        pos = self.__calculatePosition(hashCode)

        slot = []

        if self.array[pos] != None:
            slot = self.array[pos]
        
        return slot
    
    def __calculatePosition(self, hashCode):
        return hashCode % len(self.array)
    
    def __removeValueFromArray(self, arr, value):
        if len(arr) != 0:
            removeElem = self.__getObjFromArray(arr, value)

            if removeElem is not None:
                arr.remove(removeElem) 
    
    def __getObjFromArray(self, arr, value):

        removeElem = None
        for elem in arr:
            if elem == value:
                return elem
        return None

    def remove(self, obj):
        if obj is None:
            return
        
        targetSlot = self.__findPosition(obj)
        self.__removeValueFromArray(targetSlot, obj)
        
    def isContain(self, obj):
        if obj is None:
            return

        slot = self.__findPosition(obj)
        return self.__getObjFromArray(slot, obj) is not None


myset = HashSet()
myset.
            

