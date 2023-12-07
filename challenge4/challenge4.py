import string

myInput = open("input.txt")
currentLine = myInput.readline()
finalScore = 0
scratchNumbers =[0]
cardNumber = 0
while len(currentLine) > 0:
    winnngNumbers = currentLine.split(':')[1].split('|')[0].split()
    hands = currentLine.split(':')[1].split('|')[1].split()
    n = -1
    for k in hands:
        for j in winnngNumbers:
            if j==k:
                n += 1
    while len(scratchNumbers) <= cardNumber:
        scratchNumbers.append(0)
    scratchNumbers[cardNumber] += 1
    if n>=0:
        finalScore += pow(2,n)
        j = 1
        print(n+1)
        print(scratchNumbers)
        while j <= n+1:
            while len(scratchNumbers)<=j+cardNumber:
                scratchNumbers.append(0)
            scratchNumbers[j+cardNumber] += scratchNumbers[cardNumber]
            print(scratchNumbers)
            j += 1
    currentLine = myInput.readline()
    cardNumber += 1
print(finalScore)
print(sum(scratchNumbers))