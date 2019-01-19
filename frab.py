def frab(n):

    if n<1:
        return None

    lastNum=2
    secondLastNum=1

    for x in range(n-2):
        tmpResult=lastNum+secondLastNum
        secondLastNum=lastNum
        lastNum=tmpResult

    return lastNum

print(frab(1))


[] sum


