print("Calculator with Bro")
further = input("Press 'y' to continue. Press 'q' to exit. ")
while further == "y":
     operator = input("Enter an operator (+ - * /):  ")
     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))

     if operator == "+":
          result = num1 + num2
          print(f"result: {round(result, 2)}")
          further = input("Press 'y' to continue. Press 'q' to exit. ")
          
     elif operator == "-":
          result = num1 - num2
          print(f"result: {round(result, 2)}")
          further = input("Press 'y' to continue. Press 'q' to exit. ")

     elif operator == "*":
          result = num1 * num2
          print(f"result: {round(result, 2)}")
          further = input("Press 'y' to continue. Press 'q' to exit. ")

     elif operator == "/":
          result = num1 / num2
          print(f"result: {round(result, 2)}")
          further = input("Press 'y' to continue. Press 'q' to exit. ")
          

print("Thank you for using today.")


