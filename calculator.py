def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return  "Error: cannot divide by zero"
    return a / b
def get_operation():
    print("/nWhat operation do you want")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter your choice (1/2/3/4): ")
    return choice

keep_going = True

while keep_going:
    # get numbers from user
    number1 = float(input("enter the first number: "))
    number2 = float(input("enter the second number: "))

    #Get operation from user
    operation = get_operation

    #Do the the calculation
    if operation == "1":
        result = add(number1, number2)
    elif operation == "2":
        result = subtract(number1, number2)
    elif operation == "3":
        result = multiply(number1, number2)
    elif operation == "4":
        result = divide(number1, number2)
    else:
        result = "invalid operation"

    #show the result
    print("\nResult:", result)
    #Ask if they want to continue
    again = input(" \nDo you want to do another calculation? (yes or no): ")
    if again.lower() != "yes":
        keep_going + False
print( "Thank you for using the calculator!")