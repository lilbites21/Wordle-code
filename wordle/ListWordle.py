words = open("wordle words.txt", "r")
list = open("wordleAnswerList.txt", "r+")
#test = open("date test.txt", "r+")

string = words.read()
words.close

# test.truncate(0)
list.truncate(0)

months = ["January", "Febuary", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]  # never actually used this but i could use the names of the months not just the number
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30,
             31, 30, 31]  # number of days in the monthes


# function for getting the date based on the number of days after a year
def monthByNumber(day, startyear):
    #! yes i know this is over engineered

    year = startyear
    month = 0

    while True:  # sees what year it is

        leapyear = False

        day -= 365  # subtracts number of days in that year

        if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):  # if a leap year its 1 extra day
            leapyear = True
            day -= 1

        if(leapyear == False) and (day <= 0):  # if day is under 0, the date must be in that year
            day += 365  # adds back the days if so
            break

        elif(leapyear == True) and (day <= 0):  # same thing but for leap year
            day += 366  # adds an extra day back
            break

        year += 1  # if not broken by being in that year, goes to next year

    for x in range(len(months)):

        # if its a leap year then...
        if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            monthDays[1] = 29  # makes febuary 1 extra day

        day -= monthDays[x]  # subtracts the num of days in that month

        if(day <= 0):  # id the day count in under 0, must be in that month
            month = x
            day += monthDays[x]  # adds back the days
            break

        monthDays[1] = 28  # always set febuary back to 28
    monthDays[1] = 28  # ALWAYS

    return month, day, year


string = string.replace(',', ' ')
string = string.replace('\"', '')  # gets rid of unwanted characters

words = []
words.append(string[0:5])  # gets first word

for x in range(len(string)):
    if(string[x] == " "):  # if i find a space, the next 5 letters are a word
        words.append(string[x+1:x+6])

pos = 0
a = 0

for x in words:
    if(x == "humor"):  # i know that humor is the answer to feb 9
        pos = a  # so i know where humor is i can find all the other dates
    a += 1  # keeps track of what word position i am in in the list

pos -= 39  # take of the 39 days befor feb 9 so i get the index of jan 1
for x in range(len(words)-pos):  # for each word after jan 1st

    # find the date that word is found it
    month, day, year = monthByNumber(x+1, 2022)

    line = (str(day) + "/" + str(month+1) + "/" + str(year) + " word is...  " +
            words[x+pos] + "\n\n")  # string to write down date and word
    list.write(line)  # writes that string
"""
for x in range (365*10): #for testing of the test date
    month,day,year = monthByNumber(x+1,1)
    line = (str(day) + "/" + str(month+1) + "/" + str(year) + "\n")
    test.write(line)
"""
