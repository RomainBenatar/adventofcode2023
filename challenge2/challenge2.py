import string

myInput = open("input.txt")
currentLine = myInput.readline()
finalSum = 0
currentId = 0
colours = ['blue','green','red']
colours_max = [14,13,12]
current_colours = [0,0,0]
current_max_colours = [0,0,0]
finalPower = 0
while len(currentLine) > 0:
	numberIndex=5
	currentId=currentLine[numberIndex]
	numberIndex += 1
	while str(currentLine[numberIndex])!=":":
		currentId = int(currentId)*10
		currentId += int(currentLine[numberIndex])
		numberIndex += 1
	indexTable=0
	possible = True
	currentLineSplit = currentLine.replace(',','').replace(';',' ;').split()
	for a in currentLineSplit:
		j = 0
		for c in colours:
			if a == "Game":
				current_max_colours[j]=0
			if a ==";" or a == "Game":
				current_colours[j] = 0
			if c == a:
				current_colours[j] += int(currentLineSplit[indexTable-1])
			if int(current_colours[j])>int(colours_max[j]):
				possible=False
			if int(current_colours[j])>current_max_colours[j]:
				current_max_colours[j] = current_colours[j]
			j += 1
		indexTable +=1
	if possible:
		finalSum += int(currentId)
	finalPower+=current_max_colours[0]*current_max_colours[1]*current_max_colours[2]
	currentLine = myInput.readline()
print (finalSum)
print (finalPower)
