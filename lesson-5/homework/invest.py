def invest(amount, rate, years):
    """
    Calculate and display the investment growth over a given number of years.

    :param amount: Initial principal amount (float)
    :param rate: Annual rate of return as a decimal (float)
    :param years: Number of years to calculate (int)
    """
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

if __name__ == "__main__":
    # Prompt user for input
    principal = float(input("Enter the initial amount: "))
    annual_rate = float(input("Enter the annual rate of return (as a decimal, e.g., 0.05 for 5%): "))
    num_years = int(input("Enter the number of years: "))

    # Call the invest function with user inputs
    invest(principal, annual_rate, num_years)