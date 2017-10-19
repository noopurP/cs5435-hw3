#python version: 2.6

import sys
import random
import re
import functions as f


#password is the password read from input line
#n is an int
#outputFile is the file to write the honeywords to
def part1Algo(password, n, outputFile):
   #generate honeywords and append them to outputFile
   honeywords = []
   # Check if password is a string of sequential integers
   isSeq = False
   if password in '0123456789':
      isSeq = True
   # Check if password contains digits
   containsDigits = bool(re.search('\d',password))
   # If password contains digits get the position of the last digit
   if containsDigits:
      lastDigit = len(password)-re.search('\d',password[::-1]).start(0)-1
   # Add real password to honeywords
   honeywords.append(password)
   # If n is less than or equal to 10 randomly alter the last digit in the password
   if not isSeq and n <= 10:
      randDigit = [0,1,2,3,4,5,6,7,8,9]
      # If the password contains digits
      if containsDigits:
         # One honeyword will be password with trailing digits removed
         temp = f.stripDigits(password)
         if temp != '' and temp not in honeywords:
            honeywords.append(temp)
         # Remaining n-2 honeywords will be a random digit in place of the last digit
         randDigit.pop(int(password[lastDigit]))
         for i in range(n-len(honeywords)):
            honeywords.append(password[:lastDigit] + str(randDigit.pop(random.randint(0,len(randDigit)-1))) + password[lastDigit+1:])
      # Password contains no digits
      else:
         # One honeyword can use flipCase() modification
         if n > 2:
            temp = f.flipCase(password)
            if temp != '' and temp not in honeywords:
               honeywords.append(temp)
         # One honeyword can use leetChar() modification
         if n > 3:
            temp = f.leetChar(password)
            if temp != '' and temp not in honeywords:
               honeywords.append(temp)
         # Remaining honeywords will have a random digit appended to it
         for i in range(n-len(honeywords)):
            honeywords.append(password+str(randDigit.pop(random.randint(0,len(randDigit)-1))))
   # If n is greater than 10 randomly pick from all strategies
   else:
      dates = f.generateDates()
      years = f.generateYears()
      s = [0,1,2,3,4,5,6,7,8,9,10]
      if not containsDigits:
         s.remove(6)
      if not isSeq:
         s.remove(8)
      while len(honeywords) < n:
         strat = random.choice(s)
         # Add date-month
         if strat == 0:
            if dates:
               honeywords.append(f.addDate(password,dates))
            else:
               s.remove(0)
         # Add year
         elif strat == 1:
            if years:
               honeywords.append(f.addYear(password,years))
            else:
               s.remove(1)
         # Add random digits
         elif strat == 2:
            temp = f.addRandom(password)
            if temp != '' and temp not in honeywords:
               honeywords.append(temp)
         # Change leet characters
         elif strat == 3:
            temp = f.leetChar(password)
            if temp != '' and temp not in honeywords:
               honeywords.append(temp)
         # Randomly change first/last character case
         elif strat == 4:
            temp = f.flipCase(password)
            if temp != '' and temp not in honeywords:
               honeywords.append(temp)
         # Add special character between letter/digit
         elif strat == 5:
            temp = f.addSpecialChar(password)
            s.remove(5)
            if temp != '' and temp not in honeywords:
               honeywords.append(temp)
         # Take trailing digits off
         elif strat == 6:
            temp = f.stripDigits(password)
            s.remove(6)
            if temp != '' and temp not in honeywords:
               honeywords.append(temp)
         # Adding up to 3 random characters
         elif strat == 7:
            temp = f.addRandomChar(password)
            if temp != '' and temp not in honeywords:
               honeywords.append(temp)
         # Reverse the password if its sequential digits
         elif strat == 8:
            temp = f.reverse(password)
            s.remove(8)
            if temp != '' and temp not in honeywords:
               honeywords.append(temp)
         # Removing any character
         elif strat == 9:
            temp = f.removeChar(password)
            s.remove(9)
            if temp != '' and temp not in honeywords:
               honeywords.append(temp)
         # Removing vowels
         else:
            temp = f.removeVowels(password)
            s.remove(10)
            if temp != '' and temp not in honeywords:
               honeywords.append(temp)
   #shuffle the honeywords
   random.shuffle(honeywords)
   #print the honeywords to the output file
   toPrint = ""
   for i in honeywords:
      toPrint = toPrint + i +", "
   toPrint = toPrint[:len(toPrint)-2]
   outputFile.write(toPrint +"\n")
	
   
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
      part1Algo(password, n, outputFile)

if __name__ == "__main__": main()
