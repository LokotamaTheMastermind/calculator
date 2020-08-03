# Basic Calculator Code

# Import Statements
from calculators.basic_calculator import BasicCalculator
import time
import os

heading_text = "Welcome to the BASIC CALCULATOR"

heading_center = heading_text.center(143)

print(heading_center.upper())

print("Please type the corresponding letters to perform their functions        "
      "Didn't find what your looking for? Try typing 'none' in the text-field\n")
print("\bAlso type exit or quit at any main window to exit the console calculator\n")

calculator_function_selection = input("[+]Addition  [-]Subtraction  [*]Multiplication  [/]Division  [Squ]areroot  ["
                                      "Sq]uare  [C]uberoot |> ")

if calculator_function_selection == "+" or calculator_function_selection == "addition" or \
        calculator_function_selection == "Addition" or calculator_function_selection == "plus":

    # Calling External Addition Script
    BasicCalculator.addition()

elif calculator_function_selection == "-" or calculator_function_selection == "subtraction" or \
        calculator_function_selection == "Subtraction" or calculator_function_selection == "minus" or \
        calculator_function_selection == "subtract":

    # Calling External Subtraction Script
    BasicCalculator.subtraction()

elif calculator_function_selection == "*" or calculator_function_selection == "multiplication" or \
        calculator_function_selection == "Multiplication" or calculator_function_selection == "times" or \
        calculator_function_selection == "multiply":

    # Calling External Multiplication Script
    BasicCalculator.multiplication()

elif calculator_function_selection == "/" or calculator_function_selection == "division" or \
        calculator_function_selection == "Division" or calculator_function_selection == "divide":

    # Calling External Division Script
    BasicCalculator.division()

elif calculator_function_selection == "squ" or calculator_function_selection == "square-root" or \
        calculator_function_selection == "Square-root" or calculator_function_selection == "sqrt":

    # Calling External Square-root Script
    BasicCalculator.square_root()

elif calculator_function_selection == "sq" or calculator_function_selection == "square" or \
        calculator_function_selection == "Square" or \
        calculator_function_selection == "sq":

    # Calling External Square Script
    BasicCalculator.square()

elif calculator_function_selection == "c" or calculator_function_selection == "cube-root" or \
        calculator_function_selection == "Cube-root" or \
        calculator_function_selection == "cube" or \
        calculator_function_selection == "cbrt" or calculator_function_selection == "C":

    # Clearing the screen
    os.system("cls")

    # Calling External Cube-root Script
    time.sleep(1)
    BasicCalculator.cube_root()

    print("\nCopyright © PyCalc 2020, Plays Lokotama, All Rights Reserved".center(143))

elif calculator_function_selection == "none":
    print("\nMore list of calculator commands you can use [BETA]")
    calculator_function_selection_2 = input("[%]Percentage ")

elif calculator_function_selection == "exit" or calculator_function_selection == "quit":
    os.system("cls")
    print("\nThanks for using this python calculator, please consider contributing to this project\n")
    print("Console is now exiting ...")
    print("Console is ready to exit ...")
    time.sleep(10)
    print("\nConsole has exited !")
    exit()
