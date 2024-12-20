def find_factors(n):
    """
    Finds and prints all factors of a given positive integer.

    :param n: The positive integer to find factors for (int)
    """
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

if __name__ == "__main__":
    # Prompt the user for a positive integer
    number = int(input("Enter a positive integer: "))

    # Check if the input is valid
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        # Call the function to find and print factors
        find_factors(number)