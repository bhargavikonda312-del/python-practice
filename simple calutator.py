#SIMPLE PYTHON CALCULATOR
while True:
    print("\n----CALCULATOR----")
    print("1.Addition(+)")
    print("2.Subtraction(-)")
    print("3.Multiplication(*)")
    print("4.Division(/)")
    print("5.Exit")
    choice = input("Enter your choice(1-5):")
    if choice == 5:
        print("Calculator closed")
        break
    num1 = float(input("Enter frist number:"))
    num2 = float(input("Enter second number:"))
    if choice == 1:
        print("Result:",num1+num2)
    elif choice == 2:
        print("Result:",num1-num2)
    elif choice == 3:
        print("Result:",num1*num2)
    else:
         print("choice again")


