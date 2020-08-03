import math

"""

Basic Calculator Code

@author Plays Lokotama
@email lokotamathemastermind@gmail.com
@createdAt 6/23/2020

Description: This is the basic calculator code!

"""

"""Current imports

math (module)

"""


class BasicCalculator:
    @staticmethod
    def addition():
        # Global Variables

        # Input Variables
        first_num = input("Please enter the first number you want to add = ")
        second_num = input("Please enter the second number you want to add = ")

        # Validation Variables
        validate_first_number = first_num.isdigit()
        validate_second_number = second_num.isdigit()

        # When user enters an integer

        if validate_first_number and validate_second_number:
            results_addition_int = int(first_num) + int(second_num)
            print(f"\nThe result of your addition is = {results_addition_int}\n")
        # When the user enters a float

        elif not validate_first_number and not validate_second_number:
            results_addition_float = float(first_num) + float(second_num)
            print(f"\nThe result of your addition is = {results_addition_float}\n")

    @staticmethod
    def subtraction():
        # Global Variables

        # Input Variables

        first_num = input("Please enter the first number you want to subtract = ")
        second_num = input("Please enter the second number you want to subtract = ")

        # Validation Variables
        validate_first_number = first_num.isdigit()
        validate_second_number = second_num.isdigit()

        # When user enters an integer

        if validate_first_number and validate_second_number:
            results_subtraction_int = int(first_num) - int(second_num)
            print(f"\nThe result of your addition is = {results_subtraction_int}\n")

        # When the user enters a float

        elif not validate_first_number and not validate_second_number:
            results_subtraction_float = float(first_num) - float(second_num)
            print(f"\nThe result of your subtraction is = {results_subtraction_float}\n")

    @staticmethod
    def square():

        # Inputs
        first_num = input("Please enter the number you want to raise to the power of 2 = ")

        # Restrictions Variable
        validate_first_number = first_num.isdigit()

        # When user enters an normal digit

        if validate_first_number:
            results_square_int = math.pow(2, int(first_num))
            print(f"\nThe result of your exponential operation of 2 is = {results_square_int}\n")

        # When the user enters a decimal digit

        elif not validate_first_number:
            results_square_float = math.pow(2, int(first_num))
            print(f"\nThe result of your exponential operation of 2 is = {results_square_float}\n")

    @staticmethod
    def square_root():

        # Inputs
        first_num = input("Please enter the number you want to find the square-root of = ")

        # Restrictions Variable
        validate_first_number = first_num.isdigit()

        # When user enters an normal digit

        if validate_first_number:
            results_square_root_int = math.sqrt(int(first_num))
            print(f"\nThe result of your square-root operation is = {results_square_root_int}\n")

        # When the user enters a decimal digit

        elif not validate_first_number:
            results_square_root_float = math.sqrt(float(first_num))
            print(f"\nThe result of your square-root operation is = {results_square_root_float}\n")

    @staticmethod
    def division():
        # Global Variables

        # Input Variables
        first_num = input("Please enter the first number you want to multiply = ")
        second_num = input("Please enter the second number you want to multiply = ")

        # Validation Variables
        validate_first_number = first_num.isdigit()
        validate_second_number = second_num.isdigit()

        # When user enters an integer

        if validate_first_number and validate_second_number:
            results_multiplication_int = int(first_num) / int(second_num)
            print(f"\nThe result of your addition is = {results_multiplication_int}\n")
        # When the user enters a float

        elif not validate_first_number and not validate_second_number:
            results_multiplication_float = float(first_num) / float(second_num)
            print(f"\nThe result of your addition is = {results_multiplication_float}\n")

    @staticmethod
    def multiplication():
        # Global Variables

        # Input Variables
        first_num = input("Please enter the first number you want to multiply = ")
        second_num = input("Please enter the second number you want to multiply = ")

        # Validation Variables
        validate_first_number = first_num.isdigit()
        validate_second_number = second_num.isdigit()

        # When user enters an integer

        if validate_first_number and validate_second_number:
            results_multiplication_int = int(first_num) * int(second_num)
            print(f"\nThe result of your addition is = {results_multiplication_int}\n")
        # When the user enters a float

        elif not validate_first_number and not validate_second_number:
            results_multiplication_float = float(first_num) * float(second_num)
            print(f"\nThe result of your addition is = {results_multiplication_float}\n")

    @staticmethod
    def cube_root():
        # Global Variables
        number = input("Please enter the number you want to find the cube-root of = ")

        # Validation Variables
        validate_number = number.isdigit()

        # When a user enters an integer

        if validate_number:
            results_cube_root_int = int(number) ** (1/3)
            print(f"\nThe result of your cube-root operation is = {results_cube_root_int}")

        # When a user enters a float

        elif not validate_number:
            results_cube_root_float = float(number ** (1/3))
