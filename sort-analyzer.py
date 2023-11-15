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
    print(timeTaken)


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

number = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
def average(function_to_call, amount_of_turns_to_run):
    arrays_to_sort = [randomData, reversedData, nearlySortedData, fewUniqueData]


    for item in arrays_to_sort:

        average_list = []
        for i in range(amount_of_turns_to_run):
            copy = item[:]
            startTime = time.time()
            function_to_call(copy)
            endTime = time.time()
            timeTaken = endTime - startTime

            average_list.append(timeTaken)

        average_calculate = 0
        for item in average_list:
            average_calculate += item
        print(average_calculate)
        result = average_calculate / amount_of_turns_to_run

        print(f"average time of sorting is {result}s")



average(bubbleSort, 5)

