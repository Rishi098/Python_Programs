# Write a function named “isTheDateValid” that accepts three integers as parameters (yyyy, mm, dd); the first one is year,
# second for month number and third for day of the month and return True or False
# depending upon whether the given argument values represent a valid date or not and
# returns True or False.

# Following are examples calls and their expected results;

# isTheDateValid(2023, 5, 8) returns True,
# While calling it as isTheDateValid(2023,2,29) returns False
# And isTheDateValid(2020, 2, 29) returns True

def isTheDateValid(yyyy, mm, dd):
    if yyyy > 2000 and (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12) and dd <= 31:
        print("true")
    elif yyyy > 2000 and (mm == 4 or mm == 6 or mm == 9 or mm == 11) and dd <= 30:
        print("true")
    elif yyyy > 2000 and mm == 2 and dd <= 28:
        print("true")
    else:
        print("false")


isTheDateValid(2004, 3, 29)