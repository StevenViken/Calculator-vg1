

def calculate():
    equation = input("Equation(use spaces): ")
    splitE = equation.split(" ")
    splitE = multiply(splitE)
    splitE = divide(splitE)
    splitE = addition(splitE)
    splitE = subtract(splitE)
    print(splitE[0])

def multiply(splitE):
    i = 0
    while i < len(splitE):
        if splitE[i] == "*":
            multiply = int(splitE[i - 1]) * int(splitE[i + 1])
            splitE[i - 1] = multiply
            splitE.pop(i)
            splitE.pop(i)
            i = 0
        i = i + 1
    return splitE
def divide(splitE):
    i = 0
    while i < len(splitE):
        if splitE[i] == "/":
            multiply = int(splitE[i - 1]) / int(splitE[i + 1])
            splitE[i - 1] = multiply
            splitE.pop(i)
            splitE.pop(i)
            i = 0
        i = i + 1
    return splitE
def addition(splitE):
    i = 0
    while i < len(splitE):
        if splitE[i] == "+":
            multiply = int(splitE[i - 1]) + int(splitE[i + 1])
            splitE[i - 1] = multiply
            splitE.pop(i)
            splitE.pop(i)
            i = 0
        i = i + 1
    return splitE
def subtract(splitE):
    i = 0
    while i < len(splitE):
        if splitE[i] == "-":
            multiply = int(splitE[i - 1]) - int(splitE[i + 1])
            splitE[i - 1] = multiply
            splitE.pop(i)
            splitE.pop(i)
            i = 0
        i = i + 1
    return splitE

calculate()