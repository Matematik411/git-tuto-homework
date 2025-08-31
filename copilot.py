# Kodo spodaj je generiral Copilot.


# Write me a python function that returns the nth Fibonacci number.
def fibonacci(n):
    if n < 0:
        return "Input should be a nonnegative integer."
    elif n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
# Test the function
print(fibonacci(10))  # Output: 34

# Write a function that accepts a string of 5 digits and prints them in a large font using ASCII characters.
# The print should be 7 lines tall.
def print_large_font(digits):
    if len(digits) != 5 or not digits.isdigit():
        return "Input should be a string of 5 digits."

    large_font = {
        '0': [" 000 ", "0   0", "0   0", "0   0", "0   0", "0   0", " 000 "],
        '1': ["  1  ", " 11  ", "1 1  ", "  1  ", "  1  ", "  1  ", "11111"],
        '2': [" 222 ", "2   2", "    2", "   2 ", "  2  ", " 2   ", "22222"],
        '3': [" 333 ", "3   3", "    3", " 333 ", "    3", "3   3", " 333 "],
        '4': ["4   4", "4   4", "4   4", "44444", "    4", "    4", "    4"],
        '5': ["55555", "5    ", "5    ", "5555 ", "    5", "5   5", " 555 "],
        '6': [" 666 ", "6   6", "6    ", "6666 ", "6   6", "6   6", " 666 "],
        '7': ["77777", "    7", "   7 ", "  7  ", " 7   ", "7    ", "7    "],
        '8': [" 888 ", "8   8", "8   8", " 888 ", "8   8", "8   8", " 888 "],
        '9': [" 999 ", "9   9", "9   9", " 9999", "    9", "9   9", " 999 "] 
    }

    for i in range(7):
        line = ""
        for digit in digits:
            line += large_font[digit][i] + " "
        print(line)

# Test the function
print_large_font("12345")
print("---------------------------------------")
print_large_font("67890")