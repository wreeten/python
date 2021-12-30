def isLeap(year):
    leap = False
    

    if year % 400 == 0:
        return True
    if year % 4 == 0:
        return True
    if year % 4 == 0:
        return False
    return leap
year = int(input())
print(isLeap(year))