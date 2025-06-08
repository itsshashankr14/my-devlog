#lex_auth_01269363490743091290

def display(num):
    message = ""
    if num % 3 == 0 and num % 5 == 0:
        message = "Zoom"
    elif num % 5 == 0:
        message = "Zip"
    elif num % 3 and num % 5 == 0:
        message = "Zap"
    else:
        message = "Invalid"
    return message

# Provide different values for num and test your program
message = display(9)
print(message)  # Expected Output: Zip

# Additional test cases
print(display(10))  # Expected Output: Zap
print(display(15))  # Expected Output: Zoom
print(display(7))   # Expected Output: Invalid
