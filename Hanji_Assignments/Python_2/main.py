try:
    userInput = int(input("Enter your age: "))

    if userInput < 13:
        print("You are categorized as: Child")

    elif userInput < 20:
        print("You are categorized as: Teenager")

    elif userInput < 60:
        print("You are categorized as: Adult")
    
    else:
        print("You are categorized as: Senior")


except ValueError:
    print("INVALID INPUT: Age cannot be a negative or non-integer.")
    