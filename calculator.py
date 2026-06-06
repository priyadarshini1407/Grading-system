while True:
    number1=float(input("Enter the first number: "))
    number2=float(input("Enter the second number: "))
    print("Select the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5.Exit")
    choice=int(input("Enter your choice (1/2/3/4/5): "))
    if choice==5:
        print("Exiting the calculator. Goodbye!")
        break
    elif choice==1:
        result=number1+number2
        print("The Addition of Given Two numbers is:",result)
    elif choice==2:
        result=number1-number2
        print("The Subtraction of Given Two numbers is:",result)
    elif choice==3:
        result=number1*number2
        print("Multiplication of Given Two numbers is:",result)
    elif choice==4:
        if number2==0:
            print("Denominator must be non zero")
        else:
            number2=int(input("Enter again Second number"))
        result=number1/number2
        print("The Division of Given Two numbers is:",result)
    else:
        print("Invalid Choice")