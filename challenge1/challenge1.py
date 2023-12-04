import string

myInput = open("input1.txt")
currentLine = myInput.readline()
finalSum = 0
while len(currentLine) > 0:
    print(currentLine)
    foundFirst = False
    dozen = 0
    unite = 0
    for a in currentLine:
        if a.isnumeric() and not foundFirst:
            dozen = int(a)
            foundFirst = True
        if a.isnumeric() and foundFirst:
            unite = int(a)
    finalSum += dozen*10+unite
    currentLine = myInput.readline()

print(finalSum)

