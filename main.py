import random
import math
import csv
from multiprocessing import Pool
import random
import math

def sum_list(inputList):
    i = 0
    sum = 0
    while i < len(inputList):
        sum += inputList[i]
        i += 1
    return sum


def amount_of_x_in_list(x, inputList):
    i = 0
    count = 0
    while i < len(inputList):
        if inputList[i] == x:
            count += 1
        i += 1
    return count


def operator_converter(num, reverse=False):
    operatorString = " "

    if not reverse:
        if num == 1:
            operatorString = " + "
        elif num == 2:
            operatorString = " - "
        elif num == 3:
            operatorString = " * "
        elif num == 4:
            operatorString = " / "
    else:
        if num == " + ":
            operatorString = 1
        elif num == " - ":
            operatorString = 2
        elif num == " * ":
            operatorString = 3
        elif num == " / ":
            operatorString = 4
        elif num == "+":
            operatorString = 1
        elif num == "-":
            operatorString = 2
        elif num == "*":
            operatorString = 3
        elif num == "/":
            operatorString = 4
        elif num == " +":
            operatorString = 1
        elif num == " -":
            operatorString = 2
        elif num == " *":
            operatorString = 3
        elif num == " /":
            operatorString = 4
        elif num == "+ ":
            operatorString = 1
        elif num == "- ":
            operatorString = 2
        elif num == "* ":
            operatorString = 3
        elif num == "/ ":
            operatorString = 4

    return operatorString


def difficulty_of_equation(inputList):
    # Translating the input list into individual variables.
    d1, d2, d3, p1, p2, p3, o1, o2, total = inputList

    pow_range = [13, 8, 7, 7, 11, 6, 5, 5, 7, 3, 7, 3, 3, 3, 3, 3, 7, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    dice_powers = []
    for j in [d1, d2, d3]:
        powers = []
        for i in range(pow_range[j]):
            powers.append(math.pow(j, i))
        dice_powers.append(powers)

    listOfDistances = []
    for powers in dice_powers:
        for power in powers:
            listOfDistances.append(abs(power - total))

    # Find shortest distance
    shortest_distance = min(listOfDistances)

    # Function to count occurrences of x in a list
    def amount_of_x_in_list(x, lst):
        return lst.count(x)

    zero_powers = amount_of_x_in_list(0, [p1, p2, p3])
    one_powers = amount_of_x_in_list(1, [p1, p2, p3])

    # Equation values
    equation_values = [math.pow(d1, p1), math.pow(d2, p2), math.pow(d3, p3)]

    # Find largest equation value
    largest_num = max(equation_values)
    largest_num_dist = abs(largest_num - total)

    # Calculate the smallest multiplier
    smallest_multiplier = 0

    if o1 == 3:  
        if equation_values[0] >= equation_values[1]:
            smallest_multiplier = equation_values[1] + math.sqrt(equation_values[0]) / 5
        else:
            smallest_multiplier = equation_values[0] + math.sqrt(equation_values[1]) / 5

    if o2 == 3:
        if equation_values[1] >= equation_values[2]:
            smallest_multiplier = equation_values[2] + math.sqrt(equation_values[1]) / 5
        else:
            smallest_multiplier = equation_values[1] + math.sqrt(equation_values[2]) / 5

    smallest_multiplier = max(smallest_multiplier, -1.2)


    # Difficulty variables
    difficulty_variables = [total, shortest_distance, zero_powers, one_powers, largest_num, largest_num_dist, smallest_multiplier]

    # Difficulty calculation
    new_difficulty = 4 + math.sqrt(difficulty_variables[0]) / 15 + difficulty_variables[1] / 12 - difficulty_variables[2] / 0.75 - difficulty_variables[3] / 1.25 + math.sqrt(difficulty_variables[4]) / 16 + difficulty_variables[5] / 9 + difficulty_variables[6] / 2

    if new_difficulty < 3.2:
        new_difficulty = 3.2

    return round(new_difficulty * 50) / 100


def generate_random_board(highestNum=999):
    boardNums = []

    while len(boardNums) < 36:
        nextNum = random.randint(1, highestNum)
        if amount_of_x_in_list(nextNum, boardNums) == 0:
            boardNums.append(nextNum)

    boardNums.sort()
    return boardNums


def generate_pattern_board(multiple=[6], startingNumber=6):
    boardList = []
    i = 0

    if len(multiple) == 1:
        while i < 36:
            boardList.append(startingNumber + i * multiple[0])
            i += 1
    elif len(multiple) == 2:
        while i < 18:
            boardList.append(startingNumber + i * multiple[0] + i * multiple[1])
            boardList.append(startingNumber + i * multiple[0] + i * multiple[1] + multiple[0])
            i += 1
    elif len(multiple) == 3:
        while i < 12:
            boardList.append(startingNumber + i * multiple[0] + i * multiple[1] + i * multiple[2])
            boardList.append(startingNumber + i * multiple[0] + i * multiple[1] + i * multiple[2] + multiple[0])
            boardList.append(startingNumber + i * multiple[0] + i * multiple[1] + i * multiple[2] + multiple[0] + multiple[1])
            i += 1
    return boardList


def generate_random_dice(minDice=1, maxDice=10, lastMaxDice=20):
    dice = [random.randint(minDice, maxDice), random.randint(minDice, maxDice), random.randint(minDice, lastMaxDice)]
    while amount_of_x_in_list(dice[0], dice) > 2:
        dice = [random.randint(minDice, maxDice), random.randint(minDice, maxDice),
                random.randint(minDice, lastMaxDice)]
    return dice


def calculate_equation(n1, n2, n3, o1, o2):
    if o1 == 1:
        if o2 == 1:
            return n1 + n2 + n3
        if o2 == 2:
            return n1 + n2 - n3
        if o2 == 3:
            return n1 + n2 * n3
        if o2 == 4:
            return n1 + n2 / n3
    if o1 == 2:
        if o2 == 1:
            return n1 - n2 + n3
        if o2 == 2:
            return n1 - n2 - n3
        if o2 == 3:
            return n1 - n2 * n3
        if o2 == 4:
            return n1 - n2 / n3
    if o1 == 3:
        if o2 == 1:
            return n1 * n2 + n3
        if o2 == 2:
            return n1 * n2 - n3
        if o2 == 3:
            return n1 * n2 * n3
        if o2 == 4:
            return n1 * n2 / n3
    if o1 == 4:
        if o2 == 1:
            return n1 / n2 + n3
        if o2 == 2:
            return n1 / n2 - n3
        if o2 == 3:
            return n1 / n2 * n3
        if o2 == 4:
            return n1 / n2 / n3


def cycle(x, y, z, i):
    if i == 0:
        return [x, y, z]
    elif i == 1:
        return [x, z, y]
    elif i == 2:
        return [y, x, z]
    elif i == 3:
        return [y, z, x]
    elif i == 4:
        return [z, y, x]
    elif i == 5:
        return [z, x, y]


def de_power(x):
    if x == 4 or x == 8 or x == 16:
        return 2
    elif x == 9:
        return 3
    else:
        return x


def easiest_solution(inputList):
    dice1 = de_power(inputList[0])
    dice2 = de_power(inputList[1])
    dice3 = de_power(inputList[2])
    total = inputList[3]
    p1 = 0
    p2 = 0
    p3 = 0
    o1 = 1
    o2 = 1

    i = 0

    # List of maximum exponents for each dice roll, starting at 0
    # Limiting the max individual base to 10,000.  Changed this so I can do things like 6^7/3^7
    maxExponents = [1, 1, 12, 7, 6, 6, 10, 5, 4, 4, 7, 3, 7, 3, 3, 3, 3, 3, 7, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

    # List of solutions.  Formatted normally (including the total)
    solutionsList = []

    # Current lowest difficulty achieved by an equation
    smallestDifficulty = pow(10, 10)

    # Current least difficult equation
    easiestEquation = []

    run = True

    while i < 6:

        d1 = cycle(dice1, dice2, dice3, i)[0]
        d2 = cycle(dice1, dice2, dice3, i)[1]
        d3 = cycle(dice1, dice2, dice3, i)[2]

        while run:

            if calculate_equation(pow(d1, p1), pow(d2, p2), pow(d3, p3), o1, o2) == total:
                solutionsList.append([d1, d2, d3, p1, p2, p3, o1, o2, total])
                if difficulty_of_equation([d1, d2, d3, p1, p2, p3, o1, o2, total]) < smallestDifficulty:
                    smallestDifficulty = difficulty_of_equation([d1, d2, d3, p1, p2, p3, o1, o2, total])
                    easiestEquation = [d1, d2, d3, p1, p2, p3, o1, o2, total]
            if p1 < maxExponents[d1]:
                p1 += 1
            elif p2 < maxExponents[d2]:
                p2 += 1
                p1 = 0
            elif p3 < maxExponents[d3]:
                p3 += 1
                p2 = 0
                p1 = 0
            elif o1 < 4:
                o1 += 1
                p3 = 0
                p2 = 0
                p1 = 0
            elif o2 < 4:
                o2 += 1
                o1 = 0
                p3 = 0
                p2 = 0
                p1 = 0
            else:
                run = False
        run = True
        i += 1
        o2 = 0
        o1 = 0
        p3 = 0
        p2 = 0
        p1 = 0

    return easiestEquation


def validate_user_input(firstString, errorString="Error, please enter an integer: "):
    validatedInput = 0
    tryLoop = True

    try:
        validatedInput = int(input(firstString))
    except ValueError:
        while tryLoop:
            tryLoop = False
            try:
                validatedInput = int(input(errorString))
            except ValueError:
                tryLoop = True
    return validatedInput


def validate_between_ranges(minVal, maxVal, userInput):
    while userInput < minVal or userInput > maxVal:
        userInput = validate_user_input("Error, value out of range.  Please re enter value: ")
    return userInput


def print_board(numList):
    i = 0
    while i < 6:
        print(str(numList[6 * i + 0]) + " " + str(numList[6 * i + 1]) + " " + str(numList[6 * i + 2]) + " " +
              str(numList[6 * i + 3]) + " " + str(numList[6 * i + 4]) + " " + str(numList[6 * i + 5]))
        i += 1

    i = 0


def convert_list_of_strings(inputList):
    # Converts a list of string to a list of integers
    outputList = []
    for a in inputList:
        outputList.append(int(a))
    return outputList


def check_with_multiple_strings(main, string1, string2="", string3="", string4="", string5=""):
    if string2 == "":
        string2 = string1
    if string3 == "":
        string3 = string1
    if string4 == "":
        string4 = string1
    if string5 == "":
        string5 = string1
    return main == string1 or main == string2 or main == string3 or main == string4 or main == string5



extensive_dice_list = [[1, 2, 2], [1, 2, 3], [1, 2, 5], [1, 2, 6], [1, 2, 7], [1, 2, 10], [1, 2, 11], [1, 2, 12], [1, 2, 13], [1, 2, 14], [1, 2, 15], [1, 2, 17], [1, 2, 18], [1, 2, 19], [1, 2, 20], [1, 3, 3], [1, 3, 5], [1, 3, 6], [1, 3, 7], [1, 3, 10], [1, 3, 11], [1, 3, 12], [1, 3, 13], [1, 3, 14], [1, 3, 15], [1, 3, 17], [1, 3, 18], [1, 3, 19], [1, 3, 20], [1, 5, 5], [1, 5, 6], [1, 5, 7], [1, 5, 10], [1, 5, 11], [1, 5, 12], [1, 5, 13], [1, 5, 14], [1, 5, 15], [1, 5, 17], [1, 5, 18], [1, 5, 19], [1, 5, 20], [1, 6, 6], [1, 6, 7], [1, 6, 10], [1, 6, 11], [1, 6, 12], [1, 6, 13], [1, 6, 14], [1, 6, 15], [1, 6, 17], [1, 6, 18], [1, 6, 19], [1, 6, 20], [1, 7, 7], [1, 7, 10], [1, 7, 11], [1, 7, 12], [1, 7, 13], [1, 7, 14], [1, 7, 15], [1, 7, 17], [1, 7, 18], [1, 7, 19], [1, 7, 20], [1, 10, 10], [1, 10, 11], [1, 10, 12], [1, 10, 13], [1, 10, 14], [1, 10, 15], [1, 10, 17], [1, 10, 18], [1, 10, 19], [1, 10, 20], [1, 
11, 11], [1, 11, 12], [1, 11, 13], [1, 11, 14], [1, 11, 15], [1, 11, 17], [1, 11, 18], [1, 11, 19], [1, 11, 20], [1, 12, 12], [1, 12, 13], [1, 12, 14], [1, 12, 15], [1, 12, 17], [1, 12, 18], [1, 12, 19], [1, 12, 20], [1, 13, 
13], [1, 13, 14], [1, 13, 15], [1, 13, 17], [1, 13, 18], [1, 13, 19], [1, 13, 20], [1, 14, 14], [1, 14, 15], [1, 14, 17], [1, 14, 18], [1, 14, 19], [1, 14, 20], [1, 15, 15], [1, 15, 17], [1, 15, 18], [1, 15, 19], [1, 15, 20], [1, 17, 17], [1, 17, 18], [1, 17, 19], [1, 17, 20], [1, 18, 18], [1, 18, 19], [1, 18, 20], [1, 19, 19], [1, 19, 20], [1, 20, 20], [2, 2, 2], [2, 2, 3], [2, 2, 5], [2, 2, 6], [2, 2, 7], [2, 2, 10], [2, 2, 11], [2, 2, 12], [2, 2, 13], [2, 2, 14], [2, 2, 15], [2, 2, 17], [2, 2, 18], [2, 2, 19], [2, 2, 20], [2, 3, 3], [2, 3, 5], [2, 3, 6], [2, 3, 7], [2, 3, 10], [2, 3, 11], [2, 3, 12], [2, 3, 13], [2, 3, 14], [2, 3, 15], [2, 3, 17], [2, 3, 18], [2, 
3, 19], [2, 3, 20], [2, 5, 5], [2, 5, 6], [2, 5, 7], [2, 5, 10], [2, 5, 11], [2, 5, 12], [2, 5, 13], [2, 5, 14], [2, 5, 15], [2, 5, 17], [2, 5, 18], [2, 5, 19], [2, 5, 20], [2, 6, 6], [2, 6, 7], [2, 6, 10], [2, 6, 11], [2, 6, 12], [2, 6, 13], [2, 6, 14], [2, 6, 15], [2, 6, 17], [2, 6, 18], [2, 6, 19], [2, 6, 20], [2, 7, 7], [2, 7, 10], [2, 7, 11], [2, 7, 12], [2, 7, 13], [2, 7, 14], [2, 7, 15], [2, 7, 17], [2, 7, 18], [2, 7, 19], [2, 7, 20], [2, 
10, 10], [2, 10, 11], [2, 10, 12], [2, 10, 13], [2, 10, 14], [2, 10, 15], [2, 10, 17], [2, 10, 18], [2, 10, 19], [2, 10, 20], [2, 11, 11], [2, 11, 12], [2, 11, 13], [2, 11, 14], [2, 11, 15], [2, 11, 17], [2, 11, 18], [2, 11, 
19], [2, 11, 20], [2, 12, 12], [2, 12, 13], [2, 12, 14], [2, 12, 15], [2, 12, 17], [2, 12, 18], [2, 12, 19], [2, 12, 20], [2, 13, 13], [2, 13, 14], [2, 13, 15], [2, 13, 17], [2, 13, 18], [2, 13, 19], [2, 13, 20], [2, 14, 14], [2, 14, 15], [2, 14, 17], [2, 14, 18], [2, 14, 19], [2, 14, 20], [2, 15, 15], [2, 15, 17], [2, 15, 18], [2, 15, 19], [2, 15, 20], [2, 17, 17], [2, 17, 18], [2, 17, 19], [2, 17, 20], [2, 18, 18], [2, 18, 19], [2, 18, 20], [2, 19, 19], [2, 19, 20], [2, 20, 20], [3, 3, 3], [3, 3, 5], [3, 3, 6], [3, 3, 7], [3, 3, 10], [3, 3, 11], [3, 3, 12], [3, 3, 13], [3, 3, 14], [3, 3, 15], [3, 3, 17], [3, 3, 18], [3, 3, 19], [3, 3, 20], [3, 5, 5], [3, 5, 6], [3, 5, 7], [3, 5, 10], [3, 5, 11], [3, 5, 12], [3, 5, 13], [3, 5, 14], [3, 5, 15], [3, 5, 17], [3, 5, 18], [3, 5, 19], [3, 5, 20], [3, 6, 6], [3, 6, 7], [3, 6, 10], [3, 6, 11], [3, 6, 12], [3, 6, 13], [3, 6, 14], [3, 6, 15], [3, 6, 17], [3, 6, 18], [3, 6, 19], [3, 6, 20], [3, 7, 7], [3, 7, 10], [3, 7, 11], [3, 7, 12], [3, 7, 13], [3, 7, 14], [3, 7, 15], [3, 7, 17], [3, 7, 18], [3, 7, 19], [3, 7, 20], [3, 10, 10], [3, 10, 11], [3, 10, 12], [3, 10, 13], [3, 10, 14], [3, 10, 15], [3, 10, 17], [3, 10, 18], [3, 10, 19], [3, 10, 20], [3, 11, 11], [3, 11, 12], [3, 11, 13], [3, 11, 14], [3, 11, 15], [3, 11, 17], [3, 11, 18], [3, 11, 19], [3, 11, 20], [3, 12, 12], [3, 12, 13], [3, 12, 14], [3, 12, 15], [3, 12, 17], [3, 12, 18], [3, 12, 19], [3, 12, 20], [3, 13, 13], [3, 13, 14], [3, 13, 15], [3, 13, 17], [3, 13, 18], [3, 13, 19], [3, 13, 20], [3, 14, 14], [3, 14, 15], [3, 14, 17], [3, 14, 18], [3, 14, 19], [3, 14, 20], [3, 15, 15], [3, 15, 17], [3, 15, 18], [3, 15, 19], [3, 15, 20], [3, 17, 17], [3, 17, 18], [3, 17, 19], [3, 17, 20], [3, 18, 18], [3, 18, 19], [3, 18, 20], [3, 19, 19], [3, 19, 20], [3, 20, 20], [5, 5, 5], [5, 5, 6], [5, 5, 7], [5, 5, 10], [5, 5, 11], [5, 5, 12], [5, 5, 13], [5, 5, 14], [5, 5, 15], [5, 5, 17], [5, 5, 18], [5, 5, 19], [5, 5, 20], [5, 6, 6], [5, 6, 7], [5, 6, 10], [5, 6, 11], [5, 6, 12], [5, 6, 13], [5, 6, 14], [5, 6, 15], [5, 6, 17], [5, 6, 18], [5, 6, 19], [5, 6, 20], [5, 7, 7], [5, 7, 10], [5, 7, 11], [5, 7, 12], [5, 7, 13], [5, 7, 14], [5, 7, 15], [5, 7, 17], [5, 7, 18], [5, 7, 19], [5, 7, 20], [5, 10, 10], [5, 10, 11], [5, 10, 12], [5, 10, 13], [5, 10, 14], [5, 10, 15], [5, 10, 17], [5, 10, 18], [5, 10, 19], [5, 10, 20], [5, 11, 11], [5, 11, 12], [5, 11, 13], [5, 11, 14], [5, 11, 15], [5, 11, 17], [5, 11, 18], [5, 11, 19], [5, 11, 20], [5, 12, 12], [5, 12, 13], [5, 12, 14], [5, 12, 15], [5, 12, 17], [5, 12, 18], [5, 12, 19], [5, 12, 20], [5, 13, 13], [5, 13, 14], [5, 13, 15], [5, 13, 17], [5, 13, 18], [5, 13, 19], [5, 13, 20], [5, 14, 14], [5, 14, 15], [5, 14, 17], [5, 14, 18], [5, 14, 19], [5, 14, 20], [5, 15, 15], [5, 15, 17], [5, 15, 18], [5, 15, 19], [5, 15, 20], [5, 17, 17], [5, 17, 18], [5, 17, 19], [5, 17, 20], [5, 18, 18], [5, 18, 19], [5, 18, 20], [5, 19, 19], [5, 19, 20], [5, 20, 20], [6, 6, 6], [6, 6, 7], [6, 6, 10], [6, 6, 11], [6, 6, 12], [6, 6, 13], [6, 6, 14], [6, 6, 15], [6, 6, 17], [6, 6, 18], [6, 6, 19], [6, 6, 20], [6, 7, 7], [6, 7, 10], [6, 7, 11], [6, 7, 12], [6, 7, 13], [6, 7, 14], [6, 7, 15], [6, 7, 17], [6, 7, 18], [6, 7, 19], [6, 7, 20], [6, 10, 10], [6, 10, 11], [6, 10, 12], [6, 10, 13], [6, 10, 14], [6, 10, 15], [6, 10, 17], [6, 10, 18], [6, 10, 19], [6, 10, 20], [6, 11, 11], [6, 11, 12], [6, 11, 13], [6, 11, 14], [6, 11, 15], [6, 11, 17], [6, 11, 18], [6, 11, 19], [6, 11, 20], [6, 12, 12], [6, 12, 13], [6, 12, 14], [6, 12, 15], [6, 12, 17], [6, 12, 18], [6, 12, 19], [6, 12, 20], [6, 13, 13], [6, 13, 14], [6, 13, 15], [6, 13, 17], [6, 13, 18], [6, 13, 19], [6, 13, 20], [6, 14, 14], [6, 14, 15], [6, 14, 17], [6, 14, 18], [6, 14, 19], [6, 14, 20], [6, 15, 15], [6, 15, 17], [6, 15, 18], [6, 15, 19], [6, 15, 20], [6, 17, 17], [6, 17, 18], [6, 17, 19], [6, 17, 20], [6, 18, 18], [6, 18, 19], [6, 18, 20], [6, 19, 19], [6, 19, 20], [6, 20, 20], [7, 7, 7], [7, 7, 10], [7, 7, 11], [7, 7, 12], [7, 7, 13], [7, 7, 14], [7, 7, 15], [7, 7, 17], [7, 7, 18], [7, 7, 19], [7, 7, 20], [7, 10, 10], [7, 10, 11], [7, 10, 12], [7, 10, 13], [7, 10, 14], [7, 10, 15], [7, 10, 17], [7, 10, 18], [7, 10, 19], [7, 10, 20], [7, 11, 11], [7, 11, 12], [7, 11, 13], [7, 11, 14], [7, 11, 15], [7, 11, 17], [7, 11, 18], [7, 11, 19], [7, 11, 20], [7, 12, 12], [7, 12, 13], [7, 12, 14], [7, 12, 15], [7, 12, 17], [7, 12, 18], [7, 12, 19], [7, 12, 20], [7, 13, 13], [7, 13, 14], [7, 13, 15], [7, 13, 17], [7, 13, 18], [7, 13, 19], [7, 13, 20], [7, 14, 14], [7, 14, 15], [7, 14, 17], [7, 14, 18], [7, 14, 19], [7, 14, 20], [7, 15, 15], [7, 15, 17], [7, 15, 18], [7, 15, 19], [7, 15, 20], [7, 17, 17], [7, 17, 18], [7, 17, 19], [7, 17, 20], [7, 18, 18], [7, 18, 19], [7, 18, 20], [7, 19, 19], [7, 19, 20], [7, 20, 20], [10, 10, 10], [10, 10, 11], [10, 10, 12], [10, 10, 13], [10, 10, 14], [10, 10, 15], [10, 10, 17], [10, 10, 18], [10, 10, 19], [10, 10, 20], [10, 11, 11], [10, 11, 12], [10, 11, 13], [10, 11, 14], [10, 11, 15], [10, 11, 17], [10, 11, 18], [10, 11, 19], [10, 11, 20], [10, 12, 12], [10, 12, 13], [10, 12, 14], [10, 12, 15], [10, 12, 17], [10, 12, 18], [10, 12, 19], [10, 12, 20], [10, 13, 13], [10, 13, 14], [10, 13, 15], [10, 13, 17], [10, 13, 18], [10, 13, 19], [10, 13, 20], [10, 14, 14], [10, 14, 15], [10, 14, 17], [10, 14, 18], [10, 14, 19], [10, 14, 20], [10, 15, 15], [10, 15, 17], [10, 15, 18], [10, 15, 19], [10, 15, 20], [10, 17, 17], [10, 17, 18], [10, 17, 19], [10, 17, 20], [10, 18, 18], [10, 18, 19], [10, 18, 20], [10, 19, 19], [10, 19, 20], [10, 20, 20], [11, 11, 11], [11, 11, 12], [11, 11, 13], [11, 11, 14], [11, 11, 15], [11, 11, 17], [11, 
11, 18], [11, 11, 19], [11, 11, 20], [11, 12, 12], [11, 12, 13], [11, 12, 14], [11, 12, 15], [11, 12, 17], [11, 12, 18], [11, 12, 19], [11, 12, 20], [11, 13, 13], [11, 13, 14], [11, 13, 15], [11, 13, 17], [11, 13, 18], [11, 13, 19], [11, 13, 20], [11, 14, 14], [11, 14, 15], [11, 14, 17], [11, 14, 18], [11, 14, 19], [11, 14, 20], [11, 15, 15], [11, 15, 17], [11, 15, 18], [11, 15, 19], [11, 15, 20], [11, 17, 17], [11, 17, 18], [11, 17, 19], [11, 17, 20], [11, 18, 18], [11, 18, 19], [11, 18, 20], [11, 19, 19], [11, 19, 20], [11, 20, 20], [12, 12, 12], [12, 12, 13], [12, 12, 14], [12, 12, 15], [12, 12, 17], [12, 12, 18], [12, 12, 19], [12, 12, 20], [12, 13, 13], [12, 13, 14], [12, 13, 15], [12, 13, 17], [12, 13, 18], [12, 13, 19], [12, 13, 20], [12, 14, 14], [12, 14, 15], [12, 14, 17], [12, 14, 18], [12, 14, 19], [12, 14, 20], [12, 15, 15], [12, 15, 17], [12, 15, 18], [12, 15, 19], [12, 15, 
20], [12, 17, 17], [12, 17, 18], [12, 17, 19], [12, 17, 20], [12, 18, 18], [12, 18, 19], [12, 18, 20], [12, 19, 19], [12, 19, 20], [12, 20, 20], [13, 13, 13], [13, 13, 14], [13, 13, 15], [13, 13, 17], [13, 13, 18], [13, 13, 19], [13, 13, 20], [13, 14, 14], [13, 14, 15], [13, 14, 17], [13, 14, 18], [13, 14, 19], [13, 14, 20], [13, 15, 15], [13, 15, 17], [13, 15, 18], [13, 15, 19], [13, 15, 20], [13, 17, 17], [13, 17, 18], [13, 17, 19], [13, 17, 20], [13, 18, 18], [13, 18, 19], [13, 18, 20], [13, 19, 19], [13, 19, 20], [13, 20, 20], [14, 14, 14], [14, 14, 15], [14, 14, 17], [14, 14, 18], [14, 14, 19], [14, 14, 20], [14, 15, 15], [14, 15, 17], [14, 15, 18], [14, 15, 19], [14, 15, 20], [14, 17, 17], [14, 17, 18], [14, 17, 19], [14, 17, 20], [14, 18, 18], [14, 18, 19], [14, 18, 20], [14, 19, 19], [14, 19, 20], [14, 20, 20], [15, 15, 15], [15, 15, 17], [15, 15, 18], [15, 15, 19], [15, 15, 20], [15, 17, 17], [15, 17, 18], [15, 17, 19], [15, 17, 20], [15, 18, 18], [15, 18, 19], [15, 18, 20], [15, 19, 19], [15, 19, 20], [15, 20, 20], [17, 17, 17], [17, 17, 18], [17, 17, 19], [17, 17, 20], [17, 18, 18], [17, 18, 19], 
[17, 18, 20], [17, 19, 19], [17, 19, 20], [17, 20, 20], [18, 18, 18], [18, 18, 19], [18, 18, 20], [18, 19, 19], [18, 19, 20], [18, 20, 20], [19, 19, 19], [19, 19, 20], [19, 20, 20], [20, 20, 20]]

def process_dice_roll(dice_roll):
    difficulties_for_roll = []
    for j in range(1, 2000):
        if j % 100 == 0:
            print(f"Process {dice_roll}: {j}/2000")
        solution = easiest_solution([dice_roll[0], dice_roll[1], dice_roll[2], j])
        if len(solution) > 0:
            difficulty = difficulty_of_equation(solution)
        else:
            difficulty = -1
        difficulties_for_roll.append(difficulty)
    return difficulties_for_roll

def main():
    pool = Pool()
    difficulties = pool.map(process_dice_roll, extensive_dice_list)
    
    with open('difficulties.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in difficulties:
            writer.writerow(row)

if __name__ == "__main__":
    main()
