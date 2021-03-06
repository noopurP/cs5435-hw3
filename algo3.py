import sys
import random

#password is the password read from input line
#n is an int
#outputFile is the file to write the honeywords to




def part3Algo(password, n, outputFile, myDataSet, topOneHundred, myDataArray):
	#generate honeywords and append them to outputFile
	honeywords = []
	if password in myDataSet:
		if password in topOneHundred:
			honeywords = part2Algo()
		else:
			honeywords = createWindow(password, n, myDataArray)
	else:
		honeywords = part1Algo()

	#print the honeywords to the output file
	toPrint = ""
	for i in honeywords:
		toPrint = toPrint + i +", "
	toPrint = toPrint[:len(toPrint)-2]
	outputFile.write(toPrint +"\n")


def createWindow(password, n, myDataArray):
	realPassIndex = random.randint(0,n)
	honeywords = []
	for passwordLocation in range(len(myDataArray)):
		if myDataArray[passwordLocation] == password:
			break
	start = passwordLocation - realPassIndex
	stop = passwordLocation + n - realPassIndex
	for i in range(start, stop):
		if i == realPassIndex:
			honeywords.append(password)
		else:
			honeywords.append(myDataArray[i])
	return honeywords

def part2Algo():
	return ["part 2"]

def part1Algo():
	return ["part 1"]

#python your_program.py n input_filename output_filename
def main():
	#get the arguments passed in
	n = int(sys.argv[1])
	inputFilename = sys.argv[2]
	outputFilename = sys.argv[3]
	inputFile = open(inputFilename, "r")
	outputFile = open(outputFilename, "w")
	myDataSet =set({})
	topOneHundred = set({})
	myDataArray = [] #we need the order of passwords to create the window
	#add the whole training set to this set
	f = open("rockyou-withcount.txt","r")
	allLines = f.readlines()
	for i in range(len(allLines)):
		thisArray = allLines[i].split(' ')
		password = thisArray[len(thisArray)-1].strip()
		myDataSet.add(password)
		myDataArray.append(password)
		if i <100:
			topOneHundred.add(password)
	#read each password from the input file and call function on it to generate honey
	while True:
		password = inputFile.readline()
		if not password: break
		password = password.splitlines()[0] #remove newline char from password
		part3Algo(password, n, outputFile, myDataSet,topOneHundred, myDataArray)


if __name__ == "__main__": main()
