import string
import re

myInput = open("input.txt")
currentLine = myInput.readline()
numbers= []
posX=[]
posY=[]
currentChar=[]
charX=[]
charY=[]
gearpos=[]
j = 0
c = 0
regex= re.compile('[\=\+\-@_!#$%^&*()<>?/\\\|}{~:[\]]')

while len(currentLine) > 0:
    isANumber = False
    currentNumber = 0
    i = 0
    for a in currentLine:
        if a.isnumeric():
            if not isANumber:
                isANumber=True
                currentNumber += int(a)
                posX.append(i)
                posY.append(j)
            else:
                currentNumber *= 10
                currentNumber += int(a)
        elif isANumber and not a.isnumeric():
            numbers.append(currentNumber)
            currentNumber = 0
            isANumber = False
            posX.append(i-1)
            posY.append(j)
        if regex.search(a):
                currentChar.append(a)
                charX.append(i)
                charY.append(j)
                if a=='*':
                    gearpos.append(c)
                c += 1
        i += 1
    j += 1

    currentLine = myInput.readline()
print(numbers)
print(charX)
print(charY)
print(posX)
print(posY)
v=0
FinalSum=0
GearRatio=0
for p in numbers:
    w = 0
    partNumber = False
    for i in charX:
        if  posX[2*v]-1 <= i <= posX[2*v+1]+1 and abs(posY[2*v]-charY[w])<=1:
            partNumber = True
        w += 1
    v += 1
    if partNumber:
        FinalSum += p

for k in gearpos:
    v = 0
    count = 0
    gears =[]
    print(charX[k])
    print(charY[k])
    for p in numbers:
        if posX[2*v]-1 <= charX[k] <= posX[2*v+1]+1 and abs(posY[2*v]-charY[k])<=1:
            gears.append(p)
        v += 1
    print(gears)
    if len(gears) == 2:
        GearRatio += gears[0]*gears[1]
print(FinalSum)
print(GearRatio)