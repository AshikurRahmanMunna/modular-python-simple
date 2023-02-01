def find_max_number(myList):
    maxNumber = 0
    for item in myList:
        if item > maxNumber:
            maxNumber = item
    return maxNumber


