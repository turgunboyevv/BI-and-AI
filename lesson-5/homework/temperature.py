def convert_cel_to_far(celsius):
    """
    Convert Celsius to Fahrenheit.

    :param celsius: Temperature in degrees Celsius (float)
    :return: Temperature in degrees Fahrenheit (float)
    """
    return celsius * 9 / 5 + 32

def convert_far_to_cel(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    :param fahrenheit: Temperature in degrees Fahrenheit (float)
    :return: Temperature in degrees Celsius (float)
    """
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    # Prompt user for Fahrenheit input
    fahrenheit = float(input("77 F: "))
    celsius = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit} 44 F = {celsius:.2f} 45 C")

    # Prompt user for Celsius input
    celsius = float(input("233 C: "))
    fahrenheit = convert_cel_to_far(celsius)
    print(f"{celsius} 44 C = {fahrenheit:.2f} 67 F")