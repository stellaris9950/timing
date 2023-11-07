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

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

def timing(function_to_call, array_to_sort):
    startTime = time.time()
    function_to_call(array_to_sort)
    endTime = time.time()
    timeTaken = endTime - startTime
    return timeTaken


def bubbleSort(anArray):
    for n in range(len(anArray) - 1):
        for i in range(len(anArray) - n - 1):
            if anArray[i] > anArray[i + 1]:
                anArray[i], anArray[i + 1] = anArray[i + 1], anArray[i]

    return


def selectionSort(anArray):
    for slot in range(len(anArray) - 1):
        min_position = slot
        for i in range(min_position + 1, len(anArray)):
            if anArray[i] < anArray[min_position]:
                min_position = i
        (anArray[slot], anArray[min_position]) = (anArray[min_position], anArray[slot])


def insertionSort(anArray):
    for i in range(1, len(anArray)):
        item = anArray[i]
        previous_position = i - 1
        while previous_position >= 0 and item < anArray[previous_position]:
            anArray[previous_position + 1] = anArray[previous_position]
            previous_position -= 1
        anArray[previous_position + 1] = item


def average(function_to_call, amount_of_turns_to_run):
    arrays_to_sort = [randomData, reversedData, nearlySortedData, fewUniqueData]
    average_list = []

    for item in arrays_to_sort:
        for i in range(amount_of_turns_to_run):
            startTime = time.time()
            function_to_call(item)
            endTime = time.time()
            timeTaken = endTime - startTime

            average_list.append(timeTaken)

        average_calculate = 0
        for item in average_list:
            average_calculate += item

        result = average_calculate / amount_of_turns_to_run

        print(f"average time of sorting is {result}s")




average(bubbleSort, 5)
