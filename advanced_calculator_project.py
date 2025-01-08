# GOAL:  Advanced Calculator
# Functions Included: 
    #   Basic Arithmetic Operations
    #   Advanced Arithmetic Operations
    #   Trigonometric Functions
    #   Statistical Functions


import os
import sys
import time
import math
import cmath
import statistics
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
def basic_arithmetic_operations():
    try:
        while True:
            print("======================================================")
            print(f"{"Basic Arithmetic Operations":^50}")
            print("======================================================")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            print("======================================================")
            operator = int(input("Enter your choice (1 - 5): "))
            clear_screen()
            
            try:
                if operator == 5:
                    print("Returning To The Main Menu....")
                    time.sleep(1)
                    main()

                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if operator == 1:
                    result = num1 + num2
                    print(f"{num1} + {num2} = {result}")
                elif operator == 2:
                    result = num1 - num2
                    print(f"{num1} - {num2} = {result}")
                elif operator == 3:
                    result = num1 * num2
                    print(f"{num1} * {num2} = {result}")
                elif operator == 4:
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                    else:
                        result = num1 / num2
                        print(f"{num1} / {num2} = {result}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    except ValueError:
        print("Please Enter from (1 - 5) only: ")             
def advanced_arithmetic_operations():
    try:
        while True:
            try:
                print("======================================================")
                print(f"{"Advanced Arithmetic Operations":^50}")
                print("======================================================")
                print("1. Square Root")
                print("2. Exponentiation")
                print("3. Logarithm (Natural)")
                print("4. Logarithm (Base 10")
                print("5. Power")
                print("6. Factorial")
                print("7. Exit")
                print("======================================================")
                operator = int(input("Enter your choice (1 - 7): "))
                clear_screen()
                
                if operator == 1:
                    num = float(input("Enter the number: "))
                    if num < 0:
                        print("Error: Square root of a negative number is not defined.")
                    else:
                        result = math.sqrt(num)
                        print(f"The square root of {num} is {result}")
                elif operator == 2:
                    base = float(input("Enter the base: "))
                    exponent = float(input("Enter the exponent: "))
                    result = base ** exponent
                    print(f"{base} raised to the power of {exponent} is {result}")
                elif operator == 3:
                    num = float(input("Enter the number: "))
                    if num <= 0:
                        print("Error: Logarithm of zero or a negative number is not defined.")
                    else:
                        result = math.log(num)
                        print(f"The natural logarithm of {num} is {result}")
                elif operator == 4:
                    base = float(input("Enter the base (10 for base 10): "))
                    num = float(input("Enter the number: "))
                    if base == 10:
                        result = math.log10(num)
                        print(f"The base 10 logarithm of {num} is {result}")
                    else:
                        result = math.log(num, base)
                        print(f"The logarithm base {base} of {num} is {result}")
                elif operator == 5:
                    base = float(input("Enter the base: "))
                    num = float(input("Enter the exponent: "))
                    if base <= 0 or num < 0:
                        print("Error: Invalid input.")
                    else:
                        result = math.pow(base, num)
                        print(f"{base} raised to the power of {num} is {result}")
                elif operator == 6:
                    num = int(input("Enter the number: "))
                    if num < 0:
                        print("Error: Factorial is not defined for negative numbers.")
                    else:
                        result = math.factorial(num)
                        print(f"The factorial of {num} is {result}")
                elif operator == 7:
                    print("Returning to the Main Menu....")
                    time.sleep(1)
                    main()
            
            except ValueError:
                print("Invalid Input...Please enter a valid integer")
    except ValueError:
        print("Please Enter from (1 - 7) only: ")
def trigonometric_functions():
    try:
        while True:
            try:
                print("======================================================")
                print(f"{"Trigonometric Functions":^50}")
                print("======================================================")
                print("1. Basic Trigonometric Functions (Sine, Cosine, Tangent)")
                print("2. Reciprocal Trigonometric Functions (Cosine, Cosecant, Cotangent)")
                print("3. Inverse Trigonometric Functions (Inverse Sine, Inverse Cosine, Inverse Tangent)")
                print("4. Exit")
                print("======================================================")
                operator = int(input("Enter your choice (1 - 4): "))
                clear_screen()

                if operator == 1:
                    print("Basic Trigonometric Functions")
                    print("1. Sine")
                    print("2. Cosine")
                    print("3. Tangent")
                    trig_choice = int(input("Enter your choice (1 - 3): "))
                    angle = float(input("Enter the angle in degrees: "))
                    angle_rad = math.radians(angle)
                    
                    if trig_choice == 1:
                        result = math.sin(angle_rad)
                        print(f"Sine of {angle} degrees is {result}")
                        print(f"Sine of {angle} radians is {math.degrees(result)} degrees")
                    elif trig_choice == 2:
                        result = math.cos(angle_rad)
                        print(f"Cosine of {angle} degrees is {result}")
                        print(f"Cosine of {angle} radians is {math.degrees(result)} degrees")
                    elif choice == 3:
                        result = math.tan(angle_rad)
                        print(f"Tangent of {angle} degrees is {result}")
                        print(f"Tangent of {angle} radians is {math.degrees(result)} degrees")
                elif operator == 2:
                    print("Reciprocal Trigonometric Functions")
                    print("1. Cosine")
                    print("2. Cosecant")
                    print("3. Cotangent")
                    trig_choice = int(input("Enter your choice (1 - 3): "))
                    angle = float(input("Enter the angle in degrees: "))
                    angle_rad = math.radians(angle)
                    
                    if trig_choice == 1:
                        result = 1 / math.cos(angle_rad)
                        print(f"Cosine of {angle} degrees is {result}")
                        print(f"Cosine of {angle} radians is {math.degrees(result)} degrees")
                    elif trig_choice == 2:
                        result = 1 / math.sin(angle_rad)
                        print(f"Cosecant of {angle} degrees is {result}")
                        print(f"Cosecant of {angle} radians is {math}")
                    elif trig_choice == 3:
                        result = 1 / math.tan(angle_rad)
                        print(f"Cotangent of {angle} degrees is {result}")
                        print(f"Cotangent of {angle} radians is {math.degrees(result)} degrees")
                elif operator == 3:
                    print("Inverse Trigonometric Functions")
                    print("1. Inverse Sine")
                    print("2. Inverse Cosine")
                    print("3. Inverse Tangent")
                    trig_choice = int(input("Enter your choice (1-3): "))
                    angle = float(input("Enter the angle in degrees: "))
                    
                    if trig_choice == 1:
                        result = math.asin(angle)
                        print(f"The angle of sine is {math.degrees(result)} degrees")
                    elif trig_choice == 2:
                        result = math.acos(angle)
                        print(f"The angle of cosine is {math.degrees(result)} degrees")
                    elif choice == 3:
                        result = math.atan(angle)
                        print(f"The angle of tangent is {math.degrees(result)} degrees")
                elif operator == 4:
                    print("Returning to the Main Menu....")
                    time.sleep(1)
                    main()

            except ValueError:
                print("Invalid Input...Please enter a valid integer")
    except ValueError:
        print("Please Enter from (1 - 4) only: ")
def statistical_functions():
    try:
        while True:
            try:
                print("======================================================")
                print(f"{"Statistical Functions":^50}")
                print("======================================================")
                print("1. Mean")
                print("2. Median")
                print("3. Mode")
                print("4. Range")
                print("5. Standard Deviation")
                print("6. Exit")
                print("======================================================")
                operator = int(input("Enter your choice (1 - 6): "))
                clear_screen()
                
                if operator == 1:
                    data = input("Enter comma-separated numbers: ").split(",")
                    data = [float(num) for num in data]
                    result = sum(data) / len(data)
                    print(f"The mean of the given numbers is {result}")
                elif operator == 2:
                    data = input("Enter comma-separated numbers: ").split(",")
                    data = [float(num) for num in data]
                    data.sort()
                    if len(data) % 2 == 0:
                        median = (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2
                    else:
                        median = data[len(data) // 2]
                    print(f"The median of the given numbers is {median}")
                elif operator == 3:
                    data = input("Enter comma-separated numbers: ").split(",")
                    data = [float(num) for num in data]
                    data.sort()
                    mode = data[0]
                    max_count = 0
                    count = 1
                    for i in range(1, len(data)):
                        if data[i] == data[i-1]:
                            count += 1
                        else:
                            if count > max_count:
                                max_count = count
                                mode = data[i-1]
                            count = 1
                    if count > max_count:
                        mode = data[-1]
                    print(f"The mode of the given numbers is {mode}")
                elif operator == 4:
                    data = input("Enter comma-separated numbers: ").split(",")
                    data = [float(num) for num in data]
                    data.sort()
                    min_value = data[0]
                    max_value = data[-1]
                    range_value = max_value - min_value
                    print(f"The range of the given numbers is {range_value}")
                elif operator == 5:
                    data = input("Enter comma-separated numbers: ").split(",")
                    data = [float(num) for num in data]
                    data.sort()
                    sum_of_squares = sum([num**2 for num in data])
                    mean_of_squares = sum_of_squares / len(data)
                    standard_deviation = math.sqrt(mean_of_squares - (sum(data) / len(data))**2)
                    print(f"The standard deviation of the given numbers is {standard_deviation}")
                elif operator == 6:
                    print("Returning to the Main Menu....")
                    time.sleep(1)
                    main()  

            except ValueError:
                print("Invalid Input... Please enter a valid integer")
    except ValueError:
        print("Please Enter from (1 - 6) only: ")

def main():
    while True:
        print("======================================================")
        print(f"{"Advanced Calculator":^50}")
        print("======================================================")

        print("MENU")
        print("1. Basic Arithmetic Operations")
        print("2. Advanced Arithmetic Operations")
        print("3. Trigonometric Functions")
        print("4. Statistical Functions")
        print("5. Exit")
        print("======================================================")
        choice = input("Enter Your Choice: ")
        clear_screen()

        if choice == "1":
            basic_arithmetic_operations()
        elif choice == "2":
            advanced_arithmetic_operations()
        elif choice == "3":
            trigonometric_functions()
        elif choice == "4":
            statistical_functions()
        elif choice == "5":
            print("Exiting the Program...")
            sys.exit()
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()