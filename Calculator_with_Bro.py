print("Calculator with Bro")
operator = input("Enter an operator (+ - * /):  ")
num1 = float(input("Enter first number: \n"))
num2 = float(input("Enter second number: \n"))

if operator == "+":
          result = num1 + num2
          print(f"result: {round(result, 2)}")
elif operator == "-":
          result = num1 - num2
          print(f"result: {round(result, 2)}")
elif operator == "*":
          result = num1 * num2
          print(f"result: {round(result, 2)}")
elif operator == "/":
          result = num1 / num2
          print(f"result: {round(result, 2)}")
print("To continue press 'y' to end press 'q' ")
