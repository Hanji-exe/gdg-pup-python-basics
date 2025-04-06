myfav_Foods = [ "Adobo", "Pancit", "Biryani", "Fried Chicken", "Pizza", "Carbonara"]

print("\n Here are my favorite foods:")

print("\n")

for food in myfav_Foods :
    print(f"> {food }")

print("\n")

try:
    startNum = int(input("Enter a positive number to start the countdown: "))

    if startNum <=0:
        print("Invalid input: Please enter a number greater than zero.")
    else:
        print("\n")
        print("Countdown:")
        print("\n")

        while startNum > 0:
            print(startNum)
            startNum -= 1

        print("\nCountdown complete!")


except ValueError:
    print("Invalid input: Please enter a valid number.")
