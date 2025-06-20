import os 
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}
def calculator():
    number1 = float(input("Enter the first number: "))
    for symbol in operations_dict:
        print(symbol)
        
    continue_flag = True
    while continue_flag :
        op_symbol= input("pick an operation:")
        number2= float(input("Enter the second number: "))
        calculator_function =operations_dict[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2}={output}")

        should_contain=input(f" enter 'y' to continue calculation with {output} or 'n' to a new calaculation 'y' to exit").lower()
        if should_contain=='y':
            number1=output
        elif should_contain=='n':
             continue_flag==False
             os.system('cls')
             calculator()
        else:
            continue_flag=False
            print("Bye")
calculator()
            
