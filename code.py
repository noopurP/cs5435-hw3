import sys

#password is the password read from input line
#n is an int
#outputFile is the file to write the honeywords to
def emptySetGenerate(password, n, outputFile):
	#generate honeywords and append them to outputFile
	honeywords = [password]
	for i  in range(n):
		#create honeywords based on password
		honeywords.append("Honey Word: " + str(i))
	#print the honeywords to the output file
	toPrint = ""
	for i in honeywords:
		toPrint = toPrint + i +", "
	toPrint = toPrint[:len(toPrint)-2]
	outputFile.write(toPrint +"\n")
	
	k


#python your_program.py n input_filename output_filename
def main():
	#get the arguments passed in
	n = int(sys.argv[1])
	inputFilename = sys.argv[2]
	outputFilename = sys.argv[3]
	inputFile = open(inputFilename, "r")
	outputFile = open(outputFilename, "w")
	#read each password from the input file and call function on it to generate honey
	while True:
		password = inputFile.readline()
		if not password: break
		password = password.splitlines()[0] #remove newline char from password
		emptySetGenerate(password, n, outputFile)


if __name__ == "__main__": main()
