import random

colors = ["R", "B", "G", "Y", "W", "P"]

number_of_case = 5
tries = list()
win = False

def generateProblem():
    """Generates and returns a random set of 5 pegs"""
    input = ""
    for i in range(number_of_case):
        input += colors[random.randint(0, number_of_case)]
    return input

def check(input, solution):
    """ Compares input and the solution and outputs a mastermind-like result (black, white)"""
    white = black = 0
    for i in range(5):
        if(input[i] == solution[i]):
            black = black + 1
        if(input[i] in solution and input[i] != solution[i]):
            white = white + 1
    result = (black, white)
    tries.append((input, result))
    return result

def win(blackpeg):
    if blackpeg == number_of_case:
        global win
        win = True