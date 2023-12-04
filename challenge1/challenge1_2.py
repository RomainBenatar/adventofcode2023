import string

myInput = open("input1.txt")
currentLine = myInput.readline()
finalSum = 0
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, "filler", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
while len(currentLine) > 0:
    print(currentLine)
    dozen = len(currentLine)
    unite = len(currentLine)
    i = 1
    b = 1
    c = 1
    for a in digit:
        unite = currentLine.find(str(a))
        if 0 <= unite <= dozen:
            dozen = unite
            b = i
        i += 1
    b %= 10
    dozen = 0
    j = 1
    for a in digit:
        unite = currentLine.rfind(str(a))
        if len(currentLine) >= unite >= dozen:
            dozen = unite
            c = j
        j += 1
    c %= 10
    finalSum += (b * 10 + c)
    print(finalSum)
    currentLine = myInput.readline()

print(finalSum)
