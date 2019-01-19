def findTargetInArray(array, target):
    for index, current in enumerate(array):
        if current==target:
            return index
    else:
        return -1
        

print(findTargetInArray([2,4,6,7], 9))