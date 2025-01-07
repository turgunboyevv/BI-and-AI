# Program 1: Rounding a float number to 2 decimal places
def round_to_two_decimals():
    number = float(input("Enter a float number: "))
    print(f"Rounded to 2 decimal places: {round(number, 2)}")

# Program 2: Finding the largest and smallest of three numbers
def largest_and_smallest():
    numbers = [float(input(f"Enter number {i+1}: ")) for i in range(3)]
    print(f"Largest number: {max(numbers)}")
    print(f"Smallest number: {min(numbers)}")

# Program 3: Kilometers to meters and centimeters
def km_to_m_and_cm():
    kilometers = float(input("Enter distance in kilometers: "))
    meters = kilometers * 1000
    centimeters = meters * 100
    print(f"{kilometers} kilometers is {meters} meters or {centimeters} centimeters.")

# Program 4: Integer division and remainder
def int_division_and_remainder():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"Integer division: {num1 // num2}")
    print(f"Remainder: {num1 % num2}")

# Program 5: Celsius to Fahrenheit conversion
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} Celsius is {fahrenheit} Fahrenheit.")

# Program 6: Last digit of a number
def last_digit():
    number = int(input("Enter a number: "))
    print(f"Last digit: {abs(number) % 10}")

# Program 7: Checking if a number is even or not
def check_even():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Uncomment the functions below to run the specific programs
# round_to_two_decimals()
# largest_and_smallest()
# km_to_m_and_cm()
# int_division_and_remainder()
# celsius_to_fahrenheit()
# last_digit()
# check_even()