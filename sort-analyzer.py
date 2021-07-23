# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS


def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 20 ELEMENTS
print(randomData[0:20])
print(reversedData[0:20])
print(nearlySortedData[0:20])
print(fewUniqueData[0:20])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# arrayCopy = randomData[:]  # Make a copy to preserver original data
# startTime = time.time()
# bubbleSort(arrayCopy)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
