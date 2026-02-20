# # Simple Calculator

# # Take input from user
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# # Perform calculation
# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error! Division by zero."
# else:
#     result = "Invalid operator!"

# # Display result
# print("Result:", result)



# Simple Calculator using only if-else

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)

else:
    if op == "-":
        print("Result:", a - b)

    else:
        if op == "*":
            print("Result:", a * b)

        else:
            if op == "/":
                if b != 0:
                    print("Result:", a / b)
                else:
                    print("Error! Division by zero.")

            else:
                print("Invalid operator!")