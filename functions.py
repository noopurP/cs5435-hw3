import datetime
import random
import string
# Generate 365 different dates
def generateDates():
    numdays = 365
    base = datetime.datetime.today()
    date_list = [(base - datetime.timedelta(days=x)).strftime("%m%d") for x in range(0, numdays)]
    return date_list

# Generate years from 1900 to 2018
def generateYears():
    return list(range(1900, 2018))

# Adding date to the end
def addDate(password, dates):
    date = dates.pop(random.randint(0,len(dates)-1))
    return password + str(date)

# Adding year to the end
def addYear(password, years):
    year = years.pop(random.randint(0,len(years)-1))
    return password + str(year)

# Adding random digits
def addRandom(password):
    digits = [random.choice(range(10)) for _ in range(random.randint(1,4))]
    return password + "".join(map(str, digits))
 
# Changing leet characters
def leetChar(password):
    leetchar = { "a":"@",
                 "A": "@",
                 "b":"8",
                 "B":"8",
                 "c":"(",
                 "C":"(",
                 "e":"3",
                 "E":"3",
                 "i":"!",
                 "I":"!",
                 "o":"0",
                 "O":"0",
                 "s":"$",
                 "S":"$",
                 "w":"VV",
                 "W":"VV",
                 }
    password = list(password)
    leet = []
    for i in range(len(password)):
        if password[i] in leetchar:
           leet.append(i)
    if len(leet) > 0:
       leetIdx = random.choice(leet)
       password[leetIdx] = leetchar.get(password[leetIdx])
    return "".join(password)

# Randomly changing first/last character case
def flipCase(password):
    tmp = random.choice(range(10))
    # change the last char
    password = list(password)
    if tmp > 4:
        if password[-1] in string.digits:
            return "".join(password)
        elif password[-1] in string.ascii_lowercase:
            password[-1] = password[-1].upper()
        elif password[-1] in string.ascii_uppercase:
            password[-1] = password[-1].lower()
    else:
        if password[0] in string.digits:
            return "".join(password)
        elif password[0] in string.ascii_lowercase:
            password[0] = password[0].upper()
        elif password[0] in string.ascii_uppercase:
            password[0] = password[0].lower()
    return "".join(password)

# Adding special characters between letter/digit
def addSpecialChar(password):
   tmp = list(password)
   prevLetter = False
   idx = -1
   for i in range(len(password)):
      if tmp[i].isdigit():
         if prevLetter:
            idx = i
         prevLetter = False
      else:
         prevLetter = True
   if idx > 0:
      return password[:idx] + '-' + password[idx:]
   else:
      return password

# Stripping digits off
def stripDigits(password):
    if not password.isdigit():
       password = list(password)
       while password[-1] in string.digits:
           password.pop()
    return "".join(password)

# Adding up to 3 random chars at the password end
def addRandomChar(password):
    randomChar = [random.choice(string.ascii_letters+string.digits) for _ in range(random.randint(1,3))]
    return password + "".join(randomChar)
# Reverse if password is digits
def reverse(password):
    for char in password:
        if char not in string.digits:
            return password
    return password[::-1]

# Removing any character
def removeChar(password):
    res = []
    for i in range(len(password)):
        if password[i] in string.ascii_letters:
            continue
        res.append(password[i])
    return "".join(res)

# Removing vowels
def removeVowels(password):
    vowels = {"a", "e", "i", "o", "u"}
    res = []
    for i in range(len(password)):
        if password[i] in vowels:
            continue
        res.append(password[i])
    return "".join(res)



# Test all functions
# years = generateYears()
# dates = generateDates()
# password = "iloves&&pongebob1234"
# res = addDate(password, dates)