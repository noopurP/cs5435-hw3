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
    return range(1900, 2018)

# Adding date to the end
def addDate(password, dates):
    date = random.choice(dates)
    return password + str(date)

# Adding year to the end
def addYear(password, years):
    year = random.choice(years)
    return password + str(year)

# Adding random digits
def addRandom(password):
    digits = [random.choice(range(10)) for _ in range(4)]
    return password + "".join(map(str, digits))
# Changing leet characters

# Randomly changing first/last character case
def flipCase(password):
    tmp = random.choice(range(10))
    # change the last char
    password = list(password)
    print tmp
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
# Stripping digits off
def stripDigits(password):
    password = list(password)
    while password[-1] in string.digits:
        password.pop()
    return "".join(password)

# Adding up to 3 random chars at the password end
def addRandomChar(password):
    randomChar = [random.choice(string.ascii_letters+string.digits) for _ in range(3)]
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
