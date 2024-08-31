def binary_to_decimal_number(binary_number):
    decimal_number = 0
    exp = 0
    binary_number = int(binary_number)
    while binary_number > 0:
        decimal = binary_number % 10
        decimal_number = decimal_number + decimal * pow(2, exp)
        binary_number = binary_number // 10
        exp += 1
    return decimal_number


def decimal_to_binary_number(decimal_number):
    binary_number = ""

    while (decimal_number >0):
        remainder = decimal_number % 2
        binary = str(remainder) + binary
        decimal_number = decimal_number // 2

    return binary_number