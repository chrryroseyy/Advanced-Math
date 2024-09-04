def binary_to_decimal_number(binary_number):
    try:
        binary_number = str(binary_number)  # Convert to string to handle integer inputs
        decimal_number = 0
        exp = 0

        # Ensure the input is a valid binary number
        if not all(digit in '01' for digit in binary_number):
            raise ValueError("Input is not a valid binary number.")

        while binary_number:
            decimal = int(binary_number[-1])  # Get the last digit
            decimal_number += decimal * pow(2, exp)
            binary_number = binary_number[:-1]  # Remove the last digit
            exp += 1

        return decimal_number

    except Exception as e:
        raise ValueError(f"Error in binary to decimal conversion: {e}")


def decimal_to_binary_number(decimal_number):
    if decimal_number < 0:
        raise ValueError("Input must be a non-negative integer.")

    if decimal_number == 0:
        return "0"

    binary_number = ""

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number //= 2

    return binary_number
