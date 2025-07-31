def value(n):
    try:
        value=int(input(n))
        return value
    except ValueError:
        print("Input is not an integer")
n = value("Input an integer: ")
# Print the input value obtained from the function.
print("Input value:", n)