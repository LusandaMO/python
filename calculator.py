#ask user input for 2 numbers
number1 = float(input("please enter the first mumber: "))
number2 = float(input("please enter the second number: "))

#ask user input for mathematical operation
operation = input("please enter the operation(+,-,*,/): ") 

#perform operation and display results
if operation == '+':
  result = number1 + number2
  print(f"{number1} + {number2} = {result}")
  
elif operation == '-':
  result = number1 - number2
  print(f"{number1} - {number2} = {result}")
  
elif operation == '*':
  result = number1 * number2
  print(f"{number1} * {number2} = {result}")

elif operation == '/':
  if number2 != 0:
    result = number1 / number2
    print(f"{number1} / {number2} = {result}")
  else:
    print("error: division by zero is not allowed.")
else:
  print("error: invalid operation entered.")
